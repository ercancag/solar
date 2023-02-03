import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack( side = 'bottom' )

redbutton = tk.Button(frame, text="Red", fg="red")
redbutton.pack(side = 'left')

greenbutton = tk.Button(frame, text="green", fg="green")
greenbutton.pack( side = 'left' )

bluebutton = tk.Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = 'left' )

blackbutton = tk.Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = 'bottom')

root.mainloop()