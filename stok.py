import tkinter as tk
from tkinter import messagebox, ttk

class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class StockApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Stok Takip Programı")

        self.stocks = []

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.window, text="Stok Adı")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        self.quantity_label = tk.Label(self.window, text="Adet")
        self.quantity_label.grid(row=1, column=0)
        self.quantity_entry = tk.Entry(self.window)
        self.quantity_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.window, text="Ekle", command=self.add_stock)
        self.add_button.grid(row=2, column=0)

        self.list_button = tk.Button(self.window, text="Göster", command=self.list_stocks)
        self.list_button.grid(row=2, column=1)

        self.tree = ttk.Treeview(self.window, columns=("Stok Adı", "Adet"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Stok Adı", text="Stok Adı")
        self.tree.heading("Adet", text="Adet")
        self.tree.column("#0", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("Stok Adı", width=150, minwidth=150, stretch=tk.NO)
        self.tree.column("Adet", width=100, minwidth=100, stretch=tk.NO)
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.edit_button = tk.Button(self.window, text="Düzenle", command=self.edit_stock)
        self.edit_button.grid(row=4, column=0)

        self.delete_button = tk.Button(self.window, text="Sil", command=self.delete_stock)
        self.delete_button.grid(row=4, column=1)

    def add_stock(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        if name and quantity:
            try:
                quantity = int(quantity)
                stock = Stock(name, quantity)
                self.stocks.append(stock)
                self.name_entry.delete(0, tk.END)
                self.quantity_entry.delete(0, tk.END)
                #messagebox.showinfo("Başarılı", "Stok başarıyla eklendi.")
            except ValueError:
                messagebox.showerror("Hata", "Adet sayısal değer olmalıdır.")
        else:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")

    def list_stocks(self):
        self.tree.delete(*self.tree.get_children())
        for idx, stock in enumerate(self.stocks):
            self.tree.insert("", idx, text=idx, values=(stock.name, stock.quantity))

    def edit_stock(self):
        selected_item = self.tree.focus()
        if selected_item:
            item_id = self.tree.item(selected_item)["text"]
            stock = self.stocks[int(item_id)]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, stock.name)
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, stock.quantity)

    def delete_stock(self):
        selected_item = self.tree.focus()
        if selected_item:
            item_id = self.tree.item(selected_item)["text"]
            self.stocks.pop(int(item_id))
            self.list_stocks()

if __name__ == "__main__":
    window = tk.Tk()
    app = StockApp(window)
    window.mainloop()

