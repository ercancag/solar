import tkinter as tk
import solar
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
grafikseltasarruf = solar.tasarruf()

root = tk.Tk()

def grafik_ciz():

            f = Figure(figsize=(5,5), dpi=100)
            a = f.add_subplot(111)

            x = [1,2,3,4,5]
            y = [12*grafikseltasarruf,2.1*12*grafikseltasarruf,3.2*12*grafikseltasarruf,4.3*12*grafikseltasarruf,5.4*12*grafikseltasarruf]

            a.plot(x,y)
            a.set_xlabel("YIL")
            a.set_ylabel("Türk Lirası")
            canvas = FigureCanvasTkAgg(f, root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH , expand=True)
cizdirme_butonu = tk.Button(root,text="Çiz", command=grafik_ciz)
cizdirme_butonu.pack(side=tk.BOTTOM, fill=tk.BOTH , expand=False)

root.mainloop()