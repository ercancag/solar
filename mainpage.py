import time
import tkinter as tk
from tkinter import ttk
import webbrowser 
from tkinter import messagebox
import pyautogui

#for döngüsü
# tr_harfler = "123456789"
# for harf in tr_harfler:
#     print(harf)
#for i in range(3, 20):
    #print(i)

def open_website():
    webbrowser.open_new("http://www.caglayanmuhendislik.com")

def on_submit():
    visitor_name = visitor_name_entry.get()
    checkin_time = checkin_time_entry.get()
    checkout_time = checkout_time_entry.get()
    reason = reason_entry.get()
    # Create a new row in the table
    table.insert("", "end", values=(visitor_name, checkin_time, checkout_time, reason))
    tk.messagebox.showinfo(title="KAYIT !!", message="Kayıt BAŞARILI")


# Create the main window
root = tk.Tk()
root.geometry("1200x300")
root.title("CAGLAYAN MUH")

def ekrankayit():
    screenshot = pyautogui.screenshot()
    screenshot.save("active_window.png")





image = tk.PhotoImage(file="caglayan.png")
button = tk.Button(root, image=image, command=open_website)
button.place(x=1,y=235)

# def sayfa2():
#     root.destroy()
#     import billing_system
# def sayfa3():
#     root.destroy()
#     import stok


# Create the form
visitor_name_label = tk.Label(root, text="Ziyaretçi Adı:")
visitor_name_label.place(x=5, y=5)
visitor_name_entry = tk.Entry(root)
visitor_name_entry.place(x=115, y=5)

checkin_time_label = tk.Label(root, text="Giriş Saati:")
checkin_time_label.place(x=5, y=35)
checkin_time_entry = tk.Entry(root)
checkin_time_entry.place(x=115, y=35)

checkout_time_label = tk.Label(root, text="Çıkış Saati:")
checkout_time_label.place(x=5, y=65)
checkout_time_entry = tk.Entry(root)
checkout_time_entry.place(x=115, y=65)

reason_label = tk.Label(root, text="Ziyaret Sebebi:")
reason_label.place(x=5, y=95)
reason_entry = tk.Entry(root)
reason_entry.place(x=115, y=95)






# Create the submit button
submit_button = tk.Button(root, text="Ziyaretçi Listesine Ekle",
                                bd=2,
                                bg="lightgreen",
                                fg="black",
                                activeforeground="black",
                                activebackground="cyan",
                                font="Andalus",
                                height=2,
                                highlightcolor="purple",
                                justify="right",
                                relief="raised",
                                command=on_submit)
submit_button.place(x=55,y=160)

# Create the table
table = ttk.Treeview(root, columns=("name", "checkin", "checkout", "reason"), show="headings")
table.heading("name", text="Ziyaretçi Adı", anchor = "center")
table.heading("checkin", text="Giriş Saati")
table.heading("checkout", text="Çıkış Saati")
table.heading("reason", text="Ziyaret Sebebi")
table.place(x=330, y=5)

text_font= ("Boulder", 15, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 5
saat_label = tk.Label(root, font=text_font, bg=background, fg=foreground, bd=border_width) 
saat_label.place(x=1080,y=255)

def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    saat_label.config(text=time_live) 
    saat_label.after(100, digital_clock)

screenshot = tk.Button(root, text="Screen Shot", bg="lightgreen", fg="black", command=ekrankayit)
screenshot.place(x=800,y=250)

digital_clock()

# def sistem_bilgisi_göster():
#     import sys
#     print("\nSistemde kurulu Python'ın;")
#     print("\tana sürüm numarası:", sys.version_info.major)
#     print("\talt sürüm numarası:", sys.version_info.minor)
#     print("\tminik sürüm numarası:", sys.version_info.micro)
#     print("\nKullanılan işletim sisteminin;")
#     print("\tadı:", sys.platform)
# sistem_bilgisi_göster()

metin = "{} ve {} iyi bir ikilidir"
print(metin.format("Python", "Django"))

root.mainloop()
