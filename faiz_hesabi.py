import tkinter as tk
import time
from PIL import Image, ImageTk

root = tk.Tk()
root.title("FAİZ HESAPLAMA")
root.colormapwindows()
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
anapara_girisi = tk.Entry(frame1)
faiz_orani_girisi = tk.Entry(frame1)
vade_süresi_girisi =tk.Entry(frame1)

anapara_etiket = tk.Label(frame1, text="Anapara:",anchor='e', font=('MV Boli',16),relief=("groove"), background="aquamarine", borderwidth="3", )
faiz_orani_etiket = tk.Label(frame1, text="Faiz Oranı %:",anchor='e', font=('MV Boli',16),relief=("groove"), background="gold", borderwidth="3" )
vade_süresi_etiket = tk.Label(frame1, text="Vade Süresi (Gün):",anchor='w', font=('MV Boli',16),relief=("groove"), background="lightpink",borderwidth="3")


def hesaplama():
    anapara = int(anapara_girisi.get())
    faiz = int(faiz_orani_girisi.get())
    vadesüresi = int(vade_süresi_girisi.get())
    getiri = round(((anapara * faiz * vadesüresi) / 36500),2)
    sonuc= round((anapara + getiri),2)
    result.configure(
    text=
    f"Toplam Yatırılan Tutar: {anapara:.2f} TL\n"
    f"Faiz Getirisi:{getiri} Türk Lirası\n"
    f"Faiz Sonrası Toplam Tutar:{sonuc} Türk Lirası\n", background="lightgreen", font=('MV Boli',16))

hesapla_butonu = tk.Button(frame1, text="Hesapla", command=hesaplama, relief="sunken")
hesapla_butonu.grid(row=3,column=1)

anaparavar = tk.IntVar()
faizoranivar = tk.IntVar()
vadesüresivar = tk.Variable()

anapara_etiket.grid(row=0,column=0)
anapara_girisi.grid(row=0, column=1)
faiz_orani_etiket.grid(row=1, column=0)
faiz_orani_girisi.grid(row=1,column=1)
vade_süresi_etiket.grid(row=2,column=0)
vade_süresi_girisi.grid(row=2, column=1)

image = tk.PhotoImage(file="ercancagimza.png")

#Kanvaslar
kanvas = tk.Canvas(root, height=70, width=280)
kanvas.create_image(135, 40, image=image)
kanvas.pack(padx=10, pady=10, side="bottom")

result = tk.Label(frame2, text="",borderwidth=("15"),relief=("groove"))
result.grid(row=0,column=0)
#result.pack(side="bottom")

frame1.pack(padx=20, pady=20)
frame2.pack(padx=20, pady=20)
root.mainloop()
#denemetestgithub