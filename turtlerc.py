import tkinter as tk
import random
import turtle

root = tk.Tk()
t = turtle.Turtle()
root.geometry("500x500")
t.shape("arrow")
t.speed(2)
t.pensize(1)
t.goto(100,0)
t.goto(100,-50)
t.goto(50,-50)
t.goto(50,-100)
t.goto(100,-100)
t.goto(100,-150)
t.goto(50,-150)
t.goto(50,-200)
t.goto(100,-200)
t.goto(100,-250)
t.goto(0,-250)
t.goto(0,0)

root.mainloop()