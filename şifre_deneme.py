import tkinter as tk

def calculate():
    # hesaplama işlemini yapmak için gerekli kodlar
    print("ercancag")
def login():
    password = password_entry.get()
    if password == "ercancag":
        calculate()
        message_label.config(text="Şifre Doğru. \n Hesaplama Sonuçları:")
    else:
        message_label.config(text="Yanlış şifre, tekrar deneyin")

root = tk.Tk()
root.title("Hesap Makinesi")

password_label = tk.Label(root, text="Şifre:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Hesapla", command=login)
login_button.pack()

message_label = tk.Label(root, text="")
message_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
