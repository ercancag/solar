import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageTk, ImageGrab
import webbrowser
from tkinter.font import BOLD, ITALIC
from DovizKurlari import DovizKurlari

dovizbilgisial = DovizKurlari()
Dolar_Deger = dovizbilgisial.DegerSor("USD","ForexSelling")

anapencere = tk.Tk()
anapencere.title('Maliyet Analizi - Çağlayan Mühendislik')

çerçeve1 = tk.Frame(anapencere)
çerçeve2 = tk.Frame(anapencere)
çerçeve3 = tk.Frame(anapencere)
çerçeve4 = tk.Frame(anapencere)

def open_website():
    webbrowser.open_new("http://www.caglayanmuhendislik.com")

def hesaplama():
    if messagebox.askokcancel("Onay", "Tüm Değerleri \n Doğru Girdiğinizden \n Emin misiniz?"):
        panel_gücü = float(var1.get())
        panel_kdv = float(var2.get())
        panel_birim_fiyat_var = float(panel_birim_fiyat_girisi.get())
        usd_kur_var = float(Dolar_Deger) or float(usd_kur_girisi.get())
        panel_adet = float(panel_sayisi_girisi.get())
        src_fiyat = float(src_fiyat_girisi.get())
        diger_giderler = float(diger_giderler_giris.get())
        konstrüksiyon_girdi = float(konstrüksiyon_girisi.get())
        beton_fyt = float(beton_giris.get())
        iscilik_fyt = float(iscilik_giris.get())
        müsteri_bilgisi_al = str(müsteri_bilgisi_giris.get())
        panel_sonuc_usd = panel_gücü * panel_birim_fiyat_var * panel_kdv * panel_adet
        konstrüksiyon_fyt = panel_adet * konstrüksiyon_girdi
        toplam_maliyet_usd = panel_sonuc_usd + src_fiyat + konstrüksiyon_fyt + diger_giderler + beton_fyt + iscilik_fyt
        toplam_maliyet_tl = toplam_maliyet_usd * usd_kur_var 
        sonuc_etiketi = tk.Label(çerçeve2, font=('GeoSlab703 MdCn BT',15),padx=10, pady=10,foreground='black',
        text=f"Müşteri: Sayın " + müsteri_bilgisi_al + " \n "
        f"Panel: {panel_sonuc_usd:.2f} $          "
        f"Sürücü: {src_fiyat:.2f} $\n"
        f"Konstrüksiyon: {konstrüksiyon_fyt:.2f} $        "
        f"Diğer Giderler: {diger_giderler:.2f} $\n"
        f"Beton Maliyeti: {beton_fyt:.2f} $          "
        f"İşçilik Maliyeti: {iscilik_fyt:.2f} $\n"
        f"Toplam Maliyet: {toplam_maliyet_usd:.2f} $             "
        f"Dolar Kuru {usd_kur_var:.2f} Türk Lirası\n\n"
        f"Toplam Maliyet: {toplam_maliyet_tl:.2f} Türk Lirası\n"
        )
        sonuc_etiketi.grid(row=0,column=0,padx=1,pady=1)
        with open('maliyet_hesabi.txt', 'w') as f:
            f.write("ÇAĞLAYAN MÜHENDİSLİK LİMİTED ŞİRKETİ SİSTEM RAPORU" + "\n")
            f.write("Panel: " + '%d' % panel_sonuc_usd + " $" + "\n")
            f.write("Sürücü: " + '%d' % src_fiyat + " $" + "\n")
            f.write("Konstrüksiyon: " + '%d' % konstrüksiyon_fyt + " $" + "\n")
            f.write("Diğer Giderler: " + '%d' % diger_giderler + " $" + "\n")
            f.write("Beton Maliyeti: " + '%d' % beton_fyt + " $" + "\n")
            f.write("İşçilik Maliyeti: " + '%d' % iscilik_fyt + " $" + "\n")
            f.write("Toplam Maliyet: " + '%d' % toplam_maliyet_usd + " $" + "\n")
            f.write("Dolar Kuru: " + '%d' % usd_kur_var + " Türk Lirası" + "\n")
            f.write("Toplam Maliyet:" + '%d' % toplam_maliyet_tl + " Türk Lirası" + "\n")

var1 = tk.Variable()
var2 = tk.Variable()
var3 = tk.Variable()
var4 = tk.Variable()
var5 = tk.Variable()
var1.set(410)
var2.set(1.1)

panel_birim_fiyat_girisi = tk.Entry(çerçeve1)
panel_birim_fiyat_girisi.insert(0, 0.42)
panel_sayisi_girisi = tk.Entry(çerçeve1)
usd_kur_girisi = tk.Entry(çerçeve1)
panel_gücü_etiket = tk.Label(çerçeve1, text="Panel Gücü (Watt): ")
panel_gücü_etiket.grid(row=0,column=0)
panel_gücü_menu = tk.OptionMenu(çerçeve1, var1, 285,400,405,410,455,540,670)
panel_gücü_menu.grid(row=0,column=1)
panel_birim_fiyat_etiket = tk.Label(çerçeve1, text='Panel Birim Fiyatı ($):')
panel_birim_fiyat_etiket.grid(row=0,column=2)
panel_birim_fiyat_girisi.grid(row=0,column=3)
panel_sayisi_etiket = tk.Label(çerçeve1, text="Panel Adedi:")
panel_sayisi_etiket.grid(row=1,column=2)
panel_sayisi_girisi.grid(row=1,column=3)
panel_sayisi_girisi.insert(0,13)
panel_kdv_etiket = tk.Label(çerçeve1,text='Kdv Oranı (%)')
panel_kdv_etiket.grid(row=1,column=0)
panel_kdv_menu = tk.OptionMenu(çerçeve1,var2,1,1.1,1.18)
panel_kdv_menu.grid(row=1,column=1)
usd_kur_etiketi = tk.Label(çerçeve1, text='Usd Kuru: (TL)')
usd_kur_etiketi.grid(row=2,column=2)
usd_kur_girisi.grid(row=2,column=3)
usd_kur_girisi.insert(0,Dolar_Deger)
src_fiyat_girisi = tk.Entry(çerçeve1)
src_fiyat_girisi.insert(0,350)
src_fiyat_etiket = tk.Label(çerçeve1, text="Sürücü / İnvertör Fiyatı ($): ")
src_fiyat_etiket.grid(row=2,column=0)
src_fiyat_girisi.grid(row=2,column=1)
konstrüksiyon_etiket = tk.Label(çerçeve1, text='Panel Başına Konstrüksiyon Fiyatı: ($)')
konstrüksiyon_etiket.grid(row=3)
konstrüksiyon_girisi = tk.Entry(çerçeve1)
konstrüksiyon_girisi.insert(0,23)
konstrüksiyon_girisi.grid(row=3,column=1)
diger_giderler_etiket = tk.Label(çerçeve1, text="Diğer Giderler: ($)")
diger_giderler_etiket.grid(row=3,column=2)
diger_giderler_giris = tk.Entry(çerçeve1)
diger_giderler_giris.insert(0, 100)
diger_giderler_giris.grid(row=3,column=3)
beton_etiket = tk.Label(çerçeve1,text="Beton Maliyeti: ($)")
beton_etiket.grid(row=4,column=0)
beton_giris = tk.Entry(çerçeve1)
beton_giris.insert(0,250)
beton_giris.grid(row=4,column=1)
iscilik_etiket = tk.Label(çerçeve1,text="İşçilik Maliyeti: ($)")
iscilik_etiket.grid(row=4,column=2)
iscilik_giris = tk.Entry(çerçeve1)
iscilik_giris.grid(row=4,column=3)
iscilik_giris.insert(0,250)
müsteri_bilgisi = tk.Label(çerçeve1,text="Müşteri Bilgisi: (Ad-Soyad)")
müsteri_bilgisi.grid(row=5,column=0)
müsteri_bilgisi_giris = tk.Entry(çerçeve1)
müsteri_bilgisi_giris.grid(row=5, column=1)
hesaplama_butonu = tk.Button(çerçeve1, text='Hesapla', command=hesaplama)
hesaplama_butonu.config(font=('DIN Condensed',15), foreground="blue")
hesaplama_butonu.grid(row=8,column=0,padx=1,pady=1)

imzaimage = tk.PhotoImage(file="ercancagimza.png")
image2=Image.open('caglayan.png')
boyutluimage2 = image2.resize((270,65))
my_img=ImageTk.PhotoImage(boyutluimage2)
kanvas = tk.Canvas(çerçeve4, height=70, width=250)
kanvas.create_image(135, 40, image=imzaimage)
kanvas.pack(padx=1, pady=1,side='left')
########################### SAAT ###################################
saat_label = tk.Label(çerçeve4, font='Verdena', fg='black') 
saat_label.pack(side="right", fill=tk.X)
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S" + "\n" + "%A" + "\n" "%d/%m/%Y")
    saat_label.config(text=time_live, font=('Clarendon Blk BT',20,BOLD), background="aquamarine") 
    saat_label.after(100, digital_clock)
digital_clock()

kanvas2 = tk.Canvas(çerçeve4, height=80, width=300)
kanvas2.create_image(155, 40, image=my_img)
kanvas2.pack(padx=1, pady=1, side="right")

gowebsite = tk.Button(çerçeve1, text="Hakkında",command=open_website)
gowebsite.config(font=('DIN Condensed',15), foreground="red")
gowebsite.grid(row=8,column=3,padx=20,pady=20)

############################ Ekran Görüntüsü #################################
def ekrankayit():
    x = anapencere.winfo_rootx()
    y = anapencere.winfo_rooty()
    width = anapencere.winfo_width()
    height = anapencere.winfo_height()
    screenshot = ImageGrab.grab(bbox=(x, y, x+width, y+height))
    screenshot.save("maliyet_hesabı_ekran_kayit.png")
def take_screenshot():
    #'Emin misiniz?' mesaj kutusu göster
    if messagebox.askokcancel("Onay", "Ekran Görüntüsü \n Alınacaktır \n Emin misiniz?"):
        #Ekran görüntüsü almak için capture_screen() fonksiyonunu çağır
        anapencere.after(100, ekrankayit)
ekran_goruntusu = tk.Button(çerçeve1, text="Ekran Görüntüsü",command=take_screenshot)
ekran_goruntusu.config(font=('DIN Condensed',15), foreground="green")
ekran_goruntusu.grid(row=8,column=2)

çerçeve1.pack(padx=10,pady=10)
çerçeve2.pack(padx=10,pady=10)
çerçeve3.pack(padx=20,pady=20)
çerçeve4.pack(padx=20,pady=20)

anapencere.mainloop()