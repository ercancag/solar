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

tüketim = 0
tasarruf = 0

def open_website():
    webbrowser.open_new("http://www.caglayanmuhendislik.com")

########################## Hesaplamalar########################################
def calculate():
    güneslenme_saatleri = var1.get()
    tek_panel_gucu = var2.get()
    tüketim = int(entry.get())
    yatirim = int(entry2.get())
    elektrikfiyat = var3.get()
    sistem_gücü = tüketim / 30 / güneslenme_saatleri
    savings = tüketim * elektrikfiyat
    tasarruf = savings
    panelyuvarlama = sistem_gücü * 1000  / tek_panel_gucu / 18
    panelyuvarlama = round(panelyuvarlama)
    print(panelyuvarlama)
    gereklipanelsayisi = panelyuvarlama * 18
    tasarlanabilirsistemgücü = gereklipanelsayisi * tek_panel_gucu / 1000
    payback_period = yatirim / savings
    payback_periodmonth = payback_period / 12
    result.configure(
        text=f"Hesaplanan Sistem Gücü: {sistem_gücü:.2f} kWh\n"
        f"Gerekli Panel Sayısı: {gereklipanelsayisi:.2f} Adet\n"
        f"Tasarlanabilir Sistem Gücü: {tasarlanabilirsistemgücü:.2f} kWh\n"
        f"Amorti Süresi:(Ay) {payback_period:.2f} Ay\n"
        f"Amorti Süresi (Yıl): {payback_periodmonth:.2f} Yıl\n"
        f"Aylık Tasarruf: {tasarruf:.2f} TL\n", bg='lightgreen', font=('Helvatical bold',16))
  
    with open('sonuçlar.txt', 'w') as f:
        f.write("ÇAĞLAYAN MÜHENDİSLİK LİMİTED ŞİRKETİ SİSTEM RAPORU" + "\n")
        f.write("Hesaplanan Sistem Gücü: " + '%d' % sistem_gücü + " kWh" + "\n")
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
frame2 = tk.Frame(root)
designer_etiket = tk.Label(frame,text="Bu program Çağlayan Mühendislik Ltd. Şti. tarafından geliştirilmiştir.", foreground="red")
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
tek_panel_gucu_label = tk.Label(frame, text="Panel Gücü: (Watt)")
tek_panel_gucu_label.config(font=('Helvatical bold',16))
tek_panel_gucu_menu = tk.OptionMenu(frame, var2, 280, 405, 410, 455, 540, 670)
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
#Etiket Yerleştirmeleri
konum_etiket.grid(row=0, column=0)
konum_menu.grid(row=0, column=1)
tek_panel_gucu_label.grid(row=1, column=0)
tek_panel_gucu_menu.grid(row=1, column=1)
elektrikfiyat_label.grid(row=2,column=0)
elektrikfiyat_menu.grid(row=2, column=1)
tüketim_etiket.grid(row=3, column=0)
entry.grid(row=3, column=1)
yatirim_label.grid(row=4, column=0)
entry2.grid(row=4, column=1)
designer_etiket.grid(row=8, column=0)
#Hesaplama Butonu
calculate_button.grid(row=5, column=0)
result.grid(row=7, column=0)

frame.pack(padx=1, pady=10)
frame2.pack(padx=1, pady=1)
########### WebSite Butonu########################
gowebsite = tk.Button(frame, text="Hakkında",command=open_website)
#gowebsite.config(font=('Arial',17,BOLD))
gowebsite.grid(row=6, column=0)

###############GRAFİK PENCERESİ############
def yeni_pencere_ac():
    yeni_pencere = tk.Toplevel(root)
    yeni_pencere.title("Yeni Pencere")
    yeni_pencere.geometry('800x600')
    def grafik_ciz():
            tüketim = int(entry.get())
            elektrikfiyat = var3.get()
            savings = tüketim * elektrikfiyat
            tasarruf = savings
            f = Figure(figsize=(5,5), dpi=100)
            a = f.add_subplot(111)
            a.set_facecolor('aquamarine')
            a.set_yscale('log')
            x = [1,2,3,4,5]
            y = [12*tasarruf,2.1*12*tasarruf,3.2*12*tasarruf,4.3*12*tasarruf,5.4*12*tasarruf]
            a.plot(x,y,linewidth=5, color='red')
            a.set_title("Yıllara Göre Kazanım - Amortisman")
            a.set_autoscale_on("b")
            a.set_xlabel("YIL")
            a.set_ylabel("Türk Lirası")
            canvas = FigureCanvasTkAgg(f, yeni_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH , expand=True)
            
    cizdirme_butonu = tk.Button(yeni_pencere,text="Çiz", command=grafik_ciz)
    cizdirme_butonu.pack()
grafiksayfasıbutonu = tk.Button(frame, text="Grafik",command=yeni_pencere_ac)
grafiksayfasıbutonu.grid(row=5, column=2)


#Resimler
image2=Image.open('caglayan.png')
boyutluimage2 = image2.resize((270,65))
my_img=ImageTk.PhotoImage(boyutluimage2)
image = tk.PhotoImage(file="ercancagimza.png")

#Kanvaslar
kanvas = tk.Canvas(root, height=70, width=280)
kanvas.create_image(135, 40, image=image)
kanvas.pack(padx=10, pady=10, side="left")
kanvas2 = tk.Canvas(root, height=80, width=300)
kanvas2.create_image(155, 40, image=my_img)
kanvas2.pack(padx=10, pady=10, side="right")

######## SAAT ############################
saat_label = tk.Label(root, font='Verdena', fg='black') 
saat_label.pack(side="right", fill=tk.X)
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    saat_label.config(text=time_live, font=('Arial',30,BOLD)) 
    saat_label.after(100, digital_clock)
digital_clock()

########### Yeni Sayfa ##########
def open_python_file():
    subprocess.call(["python3", "guneslenmesuresi.py"])
open_file_button = tk.Button(frame, text="Harita", command=open_python_file)
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