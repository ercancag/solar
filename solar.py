import tkinter as tk
from tkinter.font import BOLD
import webbrowser 
from PIL import Image, ImageTk
import time
import subprocess
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

ercancaglayan = "caglayanmuhendislik"
tüketim = 0
tasarruf = 0

def open_website():
    webbrowser.open_new("http://www.caglayanmuhendislik.com")

########################## Hesaplamalar########################################
def calculate():
    sunshine_hours = var1.get()
    panel_power = var2.get()
    tüketim = int(entry.get())
    yatirim = int(entry2.get())
    elektrikfiyat = var3.get()
    system_power = tüketim / 30 / sunshine_hours
    savings = tüketim * elektrikfiyat
    tasarruf = savings
    panelyuvarlama = system_power * 1000  / panel_power / 18
    panelyuvarlama = round(panelyuvarlama)
    print(panelyuvarlama)
    gereklipanelsayisi = panelyuvarlama * 18
    tasarlanabilirsistemgücü = gereklipanelsayisi * panel_power / 1000
    payback_period = yatirim / savings
    payback_periodmonth = payback_period / 12
    result.configure(
        text=f"Hesaplanan Sistem Gücü: {system_power:.2f} kWh\n"
        f"Gerekli Panel Sayısı: {gereklipanelsayisi:.2f} Adet\n"
        f"Tasarlanabilir Sistem Gücü: {tasarlanabilirsistemgücü:.2f} kWh\n"
        f"Amorti süresi:(Ay) {payback_period:.2f} Ay\n"
        f"Amorti süresi (Yıl): {payback_periodmonth:.2f} Yıl\n"
        f"Aylık tasarruf: {tasarruf:.2f} TL\n")
    result2.configure(
        text="Bu Program\n"
        "Çağlayan Mühendislik\n"
        "Limited Şirketi tarafından\n"
        "Geliştirilmiştir\n"
        "\n"
        "")
    with open('sonuçlar.txt', 'w') as f:
        f.write("ÇAĞLAYAN MÜHENDİSLİK LİMİTED ŞİRKETİ SİSTEM RAPORU" + "\n")
        f.write("Hesaplanan Sistem Gücü: " + '%d' % system_power + " kWh" + "\n")
        f.write("Gerekli Panel Sayısı: " + '%d' % gereklipanelsayisi + " Adet" + "\n")
        f.write("Tasarlanabilir Sistem Gücü: " + '%d' % tasarlanabilirsistemgücü + " kWh" + "\n")
        f.write("Amorti süresi:(Ay): " + '%d' % payback_period + " Ay" + "\n")
        f.write("Amorti süresi:(Yıl): " + '%d' % payback_periodmonth + " Yıl" + "\n")
        f.write("Aylık Tasarruf: " + '%d' % tasarruf + " Türk Lirası" + "\n")
        
    
#############################################################################


# Ana Pencereyi Oluşturma
root = tk.Tk()
root.title("Güneş Enerjisi Sistem Tasarımı -- designed by ercancag")
# Widgets Oluşturma



frame = tk.Frame(root)
var1 = tk.Variable()
var2 = tk.IntVar()
var3 = tk.Variable()
var1.set(7.1)
var2.set(410)
var3.set(4.5)
# Location dropdown
konum_etiket = tk.Label(frame, text="Güneşlenme Süresi: (Saat)")
konum_menu = tk.OptionMenu(frame, var1, 4,4.5,5,5.5,6,6.5,7,7.5,8,8.5)
konum_etiket.config(font=('MV Boli',16))

# Panel power dropdown
panel_power_label = tk.Label(frame, text="Panel Gücü: (Watt)")
panel_power_label.config(font=('Helvatical bold',16))
panel_power_menu = tk.OptionMenu(frame, var2, 280, 405, 410, 455, 540, 670)
elektrikfiyat_label = tk.Label(frame, text="Güncel Elektrik Fiyatı (TL):")
elektrikfiyat_label.config(font=('Helvatical bold',16))
elektrikfiyat_menu = tk.OptionMenu(frame, var3, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6)

#Tüketim Bilgisi Girişi
tüketim_etiket = tk.Label(frame, text="Aylık Tüketim (kWh):")
tüketim_etiket.config(font=('Helvatical bold',16))
entry = tk.Entry(frame)

#Yatırım Girişi
yatirim_label = tk.Label(frame, text="Yatırım Miktarı (TL):")
yatirim_label.config(font=('Helvatical bold',16))
entry2 = tk.Entry(frame)

#Hesaplama Butonu
calculate_button = tk.Button(frame, text="Hesapla", command=calculate)
#calculate_button.config(font=('Arial',17,BOLD), foreground="darkgreen", activeforeground="Purple")
result = tk.Label(frame, text="")
result2 = tk.Label(frame, text="")
#Etiket Yerleştirmeleri
konum_etiket.grid(row=0, column=0)
konum_menu.grid(row=0, column=1)
panel_power_label.grid(row=1, column=0)
panel_power_menu.grid(row=1, column=1)
elektrikfiyat_label.grid(row=2,column=0)
elektrikfiyat_menu.grid(row=2, column=1)
tüketim_etiket.grid(row=3, column=0)
entry.grid(row=3, column=1)
yatirim_label.grid(row=4, column=0)
entry2.grid(row=4, column=1)

#Hesaplama Butonu
calculate_button.grid(row=5, column=0)
result.grid(row=7, column=0)
result2.grid(row=7, column=1)
frame.pack(padx=20, pady=20)

########### WebSite Butonu########################
gowebsite = tk.Button(frame, text="Hakkında",command=open_website)
#gowebsite.config(font=('Arial',17,BOLD))
gowebsite.grid(row=6, column=0)

###############GRAFİK PENCERESİ############
def yeni_pencere_ac():
    yeni_pencere = tk.Toplevel(root)
    yeni_pencere.title("Yeni Pencere")
    yeni_pencere.geometry('400x400')
    def grafik_ciz():
            tüketim = int(entry.get())
            elektrikfiyat = var3.get()
            savings = tüketim * elektrikfiyat
            tasarruf = savings
            f = Figure(figsize=(5,5), dpi=100)
            a = f.add_subplot(111)
            x = [1,2,3,4,5]
            y = [12*tasarruf,2.1*12*tasarruf,3.2*12*tasarruf,4.3*12*tasarruf,5.4*12*tasarruf]
            a.plot(x,y)
            a.set_xlabel("YIL")
            a.set_ylabel("Türk Lirası")
            canvas = FigureCanvasTkAgg(f, yeni_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH , expand=True)
            print(tasarruf)
    cizdirme_butonu = tk.Button(yeni_pencere,text="Çiz", command=grafik_ciz)
    cizdirme_butonu.pack()
grafiksayfasıbutonu = tk.Button(root, text="Grafik",command=yeni_pencere_ac)
grafiksayfasıbutonu.pack()


#Resimler
image2=Image.open('caglayan.png')
boyutluimage2 = image2.resize((270,65))
my_img=ImageTk.PhotoImage(boyutluimage2)
image = tk.PhotoImage(file="ercancagimza.png")

#Kanvaslar
kanvas = tk.Canvas(root, height=70, width=280)
kanvas.create_image(135, 40, image=image)
kanvas.pack(padx=10, pady=10)
kanvas2 = tk.Canvas(root, height=80, width=300)
kanvas2.create_image(155, 40, image=my_img)
kanvas2.pack(padx=10, pady=10)

######## SAAT ############################
saat_label = tk.Label(root, font='Verdena', fg='black') 
saat_label.pack()
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    saat_label.config(text=time_live, font=('Arial',30,BOLD)) 
    saat_label.after(100, digital_clock)
digital_clock()

########### Yeni Sayfa ##########
def open_python_file():
    subprocess.call(["python3", "guneslenmesuresi.py"])
open_file_button = tk.Button(frame, text="Türkiye Güneşlenme Süresi Haritası", command=open_python_file)
#open_file_button.config(font=("Verdena",17,BOLD), foreground='blue')
open_file_button.grid(row=5, column=1)

#yazdırma 
def yazdir():
    filename = "sonuçlar.txt" # yazdırılacak dosyanın adı
    subprocess.run(["lpr", filename])
yazdirbutonu = tk.Button(frame, text="Sonuçları Yazdır", command=yazdir)
yazdirbutonu.grid(row=6, column=1, sticky='E')
#yazdirbutonu.config(font=('Verdena',17,BOLD), bg='green', foreground="red")










root.mainloop()