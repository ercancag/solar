import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
from tkinter import messagebox
import time
from tkinter.font import BOLD, ITALIC

def hesaplama():
    try:
        kredi_tutari = float(kredi_tutari_girisi.get())
        kkdf_bsmv = 1.20
        faiz_orani = float(faiz_orani_girisi.get()) / 100.0 * kkdf_bsmv
        taksit_sayisi = int(taksit_sayisi_girisi.get())
        taksit_miktari = float((kredi_tutari * faiz_orani * (1 + faiz_orani)**taksit_sayisi) / ((1 + faiz_orani)**taksit_sayisi - 1))

        toplam_tutar = taksit_miktari*taksit_sayisi

        # Taksit tablosu oluşturma
        taksit_tablosu = tk.Label(çerçeve1, text="Anapara\t    Faiz\t  Taksit\tKalan Borç", font=("Arial", 14),bg="#98F5FF")
        taksit_tablosu.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        kalan_borc = kredi_tutari
        for i in range(taksit_sayisi):
            faiz_tutari = kalan_borc * faiz_orani
            anapara_tutari = taksit_miktari - faiz_tutari
            kalan_borc -= anapara_tutari

            taksit_satiri = "{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(anapara_tutari, faiz_tutari, taksit_miktari, kalan_borc)
            taksit_satiri_widget = tk.Label(çerçeve1, text=taksit_satiri, font=("Arial", 14),background="#CAFF70")
            taksit_satiri_widget.grid(row=i+6, column=0, columnspan=2, padx=5, pady=5)

        sonuc.config(text="Taksit Tutarı: {:.2f} TL\nToplam Ödenecek Tutar: {:.2f} TL".format(taksit_miktari, toplam_tutar), bg="aquamarine", fg="black")
    except ValueError:
        sonuc.config(text="Lütfen geçerli bir değer girin.", fg="red")

# Ana pencere oluşturma
ana_pencere = tk.Tk()
ana_pencere.title("Kredi Hesaplama")
çerçeve1 = tk.Frame(ana_pencere)
çerçeve2 = tk.Frame(ana_pencere)
çerçeve3 = tk.Frame(ana_pencere)
çerçeve4 = tk.Frame(ana_pencere)
# Girdi alanları için etiketler ve girdi kutuları oluşturma
kredi_tutari_etiket = tk.Label(çerçeve1, text="Kredi Tutarı:", font=("Arial", 14),width="16",background="#E3CF57",height="1")
kredi_tutari_etiket.grid(row=0, column=0)

kredi_tutari_girisi = tk.Entry(çerçeve1, font=("Arial", 14),width="10")
kredi_tutari_girisi.insert(0,10000)
kredi_tutari_girisi.grid(row=0, column=1)

faiz_orani_etiket = tk.Label(çerçeve1, text="Aylık Faiz Oranı (%):", font=("Arial", 14),width="16",background="#E3CF57")
faiz_orani_etiket.grid(row=1, column=0)

faiz_orani_girisi = tk.Entry(çerçeve1, font=("Arial", 14),width="10")
faiz_orani_girisi.insert(0,1.79)
faiz_orani_girisi.grid(row=1, column=1)

taksit_sayisi_etiket = tk.Label(çerçeve1, text="Taksit Sayısı:", font=("Arial", 14),width="16",background="#E3CF57")
taksit_sayisi_etiket.grid(row=2, column=0)

taksit_sayisi_girisi = tk.Entry(çerçeve1, font=("Arial", 14),width="10")
taksit_sayisi_girisi.insert(0,12)
taksit_sayisi_girisi.grid(row=2, column=1)

# Hesapla butonunu oluşturma
hesapla_butonu = tk.Button(çerçeve1, text="Hesapla", font=("Arial", 14), command=hesaplama)
hesapla_butonu.grid(row=3, column=0, padx=5, pady=5)

# Sonuç alanını oluşturma
sonuc = tk.Label(çerçeve1, text="", font=("Arial", 14))
sonuc.grid(row=4, column=0, columnspan=2, padx=5, pady=5)



def ekrankayit():
    x = çerçeve1.winfo_rootx()
    y = çerçeve1.winfo_rooty()
    width = çerçeve1.winfo_width()
    height = çerçeve1.winfo_height()
    screenshot = ImageGrab.grab(bbox=(x, y, x+width, y+height))
    screenshot.save("kredi_sonucu.png")
def take_screenshot():
    #'Emin misiniz?' mesaj kutusu göster
    if messagebox.askokcancel("Onay", "Ekran Görüntüsü \n Alınacaktır \n Emin misiniz?"):
        #Ekran görüntüsü almak için capture_screen() fonksiyonunu çağır
        çerçeve1.after(100, ekrankayit)
ekran_goruntusu = tk.Button(çerçeve1, text="Ekran Görüntüsü Al",command=take_screenshot)
ekran_goruntusu.grid(row=3,column=1)


imzaimage = tk.PhotoImage(file="ercancagimza.png")
image2=Image.open('caglayan.png')
boyutluimage2 = image2.resize((270,65))
my_img=ImageTk.PhotoImage(boyutluimage2)
kanvas = tk.Canvas(çerçeve2, height=70, width=250)
kanvas.create_image(135, 40, image=imzaimage)
kanvas.pack(padx=1, pady=1,side='bottom')
kanvas2 = tk.Canvas(çerçeve3, height=80, width=300)
kanvas2.create_image(155, 40, image=my_img)
kanvas2.pack(padx=1, pady=1, side="bottom")
########################### SAAT ###################################
saat_label = tk.Label(çerçeve4, font='Verdena', fg='black') 
saat_label.pack(side="right", fill=tk.X)
günler = time.strftime("%A")
if günler == "Saturday": 
    gün = "Cumartesi"
elif günler == "Sunday":
    gün = "Pazar"
elif günler == "Monday":
    gün = "Pazartesi"
elif günler == "Tuesday":
    gün = "Salı"
elif günler == "Wednesday":
    gün = "Çarşamba"
elif günler == "Thursday":
    gün = "Perşembe"
elif günler == "Friday":
    gün = "Cuma"
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S" + "   " + gün + "   " "%d/%m/%Y")
    saat_label.config(text=time_live, font=('Clarendon Blk BT',20,BOLD), background="#DC143C",fg="white") 
    saat_label.after(100, digital_clock)
digital_clock()




çerçeve1.pack()
çerçeve2.pack()
çerçeve3.pack()
çerçeve4.pack()
# Ana döngüyü başlatma
ana_pencere.mainloop()


