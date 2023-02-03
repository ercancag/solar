import serial
import time
from tkinter import *
from tkinter import ttk

ser = serial.Serial('COM5', 115200) # seri port ve baud rate

root = Tk()
root.title("Serial Data Receiver")
root.geometry("300x100")
root.configure(bg="lightgreen")

value_label = ttk.Label(root, text="Waiting for data...", border=4)
value_label.pack()

def read_data():
    data = ser.readline().decode().strip() # seri porttan veriyi oku
    value_label.config(text=data) # etiketi veri ile güncelle
    root.after(1000, read_data) # 1 saniye sonra fonksiyonu tekrar çağır

read_data()

root.mainloop()