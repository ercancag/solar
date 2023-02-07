import tkinter as tk
import time
from PIL import Image, ImageTk
import webbrowser
from tkinter.font import BOLD, ITALIC
anapencere = tk.Tk()
anapencere.title('Maliyet Analizi - Çağlayan Mühendislik')

çerçeve1 = tk.Frame(anapencere)
çerçeve2 = tk.Frame(anapencere)
çerçeve3 = tk.Frame(anapencere)
çerçeve4 = tk.Frame(anapencere)

def open_website():
    webbrowser.open_new("http://www.caglayanmuhendislik.com")

def hesaplama():
    panel_gücü = float(var1.get())
    panel_kdv = float(var2.get())
    panel_birim_fiyat_var = float(panel_birim_fiyat_girisi.get())
    usd_kur_var = float(usd_kur_girisi.get())
    panel_adet = float(panel_sayisi_girisi.get())
    src_fiyat = float(src_fiyat_girisi.get())
    diger_giderler = float(diger_giderler_giris.get())
    konstrüksiyon_girdi = float(konstrüksiyon_girisi.get())
    panel_sonuc_usd = panel_gücü * panel_birim_fiyat_var * panel_kdv * panel_adet
    konstrüksiyon_fyt = panel_adet * konstrüksiyon_girdi
    toplam_maliyet_usd = panel_sonuc_usd + src_fiyat + konstrüksiyon_fyt + diger_giderler
    toplam_maliyet_tl = toplam_maliyet_usd * usd_kur_var
    sonuc_etiketi = tk.Label(çerçeve2, font=('savoye let',30),padx=10, pady=10,foreground='black',
    text=f"Panel: {panel_sonuc_usd:.2f} $          "
    f"Sürücü: {src_fiyat:.2f} $\n"
    f"Konstrüksiyon: {konstrüksiyon_fyt:.2f} $          "
    f"Diğer Giderler: {diger_giderler:.2f} $\n"
    f"Toplam Maliyet: {toplam_maliyet_usd:.2f} $\n"
    f"Toplam Maliyet: {toplam_maliyet_tl:.2f} Türk Lirası\n"
    )
    sonuc_etiketi.grid(row=0,column=0,padx=20,pady=20)

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
usd_kur_girisi.insert(0,18.95)
src_fiyat_girisi = tk.Entry(çerçeve1)
src_fiyat_girisi.insert(0,350)
src_fiyat_etiket = tk.Label(çerçeve1, text="Sürücü / İnvertör Fiyatı (USD): ")
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
diger_giderler_giris.insert(0, 350)
diger_giderler_giris.grid(row=3,column=3)

hesaplama_butonu = tk.Button(çerçeve1, text='Hesapla', command=hesaplama)
hesaplama_butonu.config(font=('Chalkduster',20,BOLD), foreground="green")
hesaplama_butonu.grid(row=6,column=0,padx=20,pady=20)

imzaimage = tk.PhotoImage(file="ercancagimza.png")
image2=Image.open('caglayan.png')
boyutluimage2 = image2.resize((270,65))
my_img=ImageTk.PhotoImage(boyutluimage2)
kanvas = tk.Canvas(çerçeve4, height=70, width=250)
kanvas.create_image(135, 40, image=imzaimage)
kanvas.pack(padx=10, pady=10,side='left')
kanvas2 = tk.Canvas(çerçeve4, height=80, width=300)
kanvas2.create_image(155, 40, image=my_img)
kanvas2.pack(padx=10, pady=10, side="right")

gowebsite = tk.Button(çerçeve1, text="Hakkında",command=open_website)
gowebsite.config(font=('Chalkduster',20,BOLD), foreground="red")
gowebsite.grid(row=6,column=3,padx=20,pady=20)

çerçeve1.pack(padx=20,pady=20)
çerçeve2.pack(padx=20,pady=20)
çerçeve3.pack(padx=20,pady=20)
çerçeve4.pack(padx=20,pady=20)

anapencere.mainloop()
#deneme caglauyan