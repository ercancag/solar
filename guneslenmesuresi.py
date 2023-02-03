import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Türkiye Güneşlenme Süresi Haritası")
root.geometry("1200x700")
gnsrsham=Image.open('guneslenmesuresi.jpg')
gnsrshamresizing = gnsrsham.resize((1100,650))
gnsrsresized=ImageTk.PhotoImage(gnsrshamresizing)

kanvas = tk.Canvas(root, height=690, width=1190)
kanvas.create_image(600, 340, image=gnsrsresized)
kanvas.pack(padx=10, pady=10)

root.mainloop()