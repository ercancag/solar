import tkinter as tk

def hesaplama():
    try:
        kredi_tutari = float(kredi_tutari_girisi.get())
        kkdf_bsmv = 1.20
        faiz_orani = float(faiz_orani_girisi.get()) / 100.0 * kkdf_bsmv
        taksit_sayisi = int(taksit_sayisi_girisi.get())
        taksit_miktari = float((kredi_tutari * faiz_orani * (1 + faiz_orani)**taksit_sayisi) / ((1 + faiz_orani)**taksit_sayisi - 1))

        toplam_tutar = taksit_miktari*taksit_sayisi

        # Taksit tablosu oluşturma
        taksit_tablosu = tk.Label(ana_pencere, text="Taksit Planı\n\nAnapara\t   Faiz\tTaksit\tKalan Borç", font=("Arial", 14))
        taksit_tablosu.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        kalan_borc = kredi_tutari
        for i in range(taksit_sayisi):
            faiz_tutari = kalan_borc * faiz_orani
            anapara_tutari = taksit_miktari - faiz_tutari
            kalan_borc -= anapara_tutari

            taksit_satiri = "{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(anapara_tutari, faiz_tutari, taksit_miktari, kalan_borc)
            taksit_satiri_widget = tk.Label(ana_pencere, text=taksit_satiri, font=("Arial", 14))
            taksit_satiri_widget.grid(row=i+6, column=0, columnspan=2, padx=5, pady=5)

        sonuc.config(text="Taksit Tutarı: {:.2f} TL\nToplam Ödenecek Tutar: {:.2f} TL".format(taksit_miktari, toplam_tutar), fg="green")
    except ValueError:
        sonuc.config(text="Lütfen geçerli bir değer girin.", fg="red")

# Ana pencere oluşturma
ana_pencere = tk.Tk()
ana_pencere.title("Kredi Hesaplama")

# Girdi alanları için etiketler ve girdi kutuları oluşturma
kredi_tutari_etiket = tk.Label(ana_pencere, text="Kredi Tutarı:", font=("Arial", 14),width="16",background="lightgreen")
kredi_tutari_etiket.grid(row=0, column=0, padx=5, pady=5)

kredi_tutari_girisi = tk.Entry(ana_pencere, font=("Arial", 14),width="10")
kredi_tutari_girisi.grid(row=0, column=1, padx=5, pady=5)

faiz_orani_etiket = tk.Label(ana_pencere, text="Aylık Faiz Oranı (%):", font=("Arial", 14),width="16",background="pink")
faiz_orani_etiket.grid(row=1, column=0, padx=5, pady=5)

faiz_orani_girisi = tk.Entry(ana_pencere, font=("Arial", 14),width="10")
faiz_orani_girisi.grid(row=1, column=1, padx=5, pady=5)

taksit_sayisi_etiket = tk.Label(ana_pencere, text="Taksit Sayısı:", font=("Arial", 14),width="16",background="lightgreen")
taksit_sayisi_etiket.grid(row=2, column=0, padx=5, pady=5)

taksit_sayisi_girisi = tk.Entry(ana_pencere, font=("Arial", 14),width="10")
taksit_sayisi_girisi.grid(row=2, column=1, padx=5, pady=5)

# Hesapla butonunu oluşturma
hesapla_butonu = tk.Button(ana_pencere, text="Hesapla", font=("Arial", 14), command=hesaplama)
hesapla_butonu.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Sonuç alanını oluşturma
sonuc = tk.Label(ana_pencere, text="", font=("Arial", 14))
sonuc.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Ana döngüyü başlatma
ana_pencere.mainloop()


