from PIL import Image, ImageFilter
from tkinter import Tk, filedialog
import cv2
import turtle
import os


root = Tk()
root.withdraw()

open_file = filedialog.askopenfilenames(filetypes=[("Image Files", ".png .jfif, .jpg, .jpeg")]) 
path = open_file[0] 
img = cv2.imread(path, 2) 
bin_image = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY ,11,2)  
hauteur = img.shape[0] 
largeur = img.shape[1]
cv2.imshow("image", bin_image) 
cv2.waitKey(0)  

screen = turtle.Screen()
screen.screensize(largeur/-2, hauteur/2)
tortue = turtle.Turtle()
screen.tracer(2,0)

for i in range(int(hauteur/2), int(hauteur/-2), -1): 
    tortue.penup() 
    tortue.goto(int(largeur/-2),i) 
    
    for l in range(int(largeur/-2), int(largeur/2)): 
        pixel_l = l + int(largeur/2) 
        pixel_h = int(hauteur/2) - i 
        if bin_image[pixel_h,pixel_l] == 0: 
            tortue.pendown()
            tortue.forward(1)
        else: 
            tortue.penup()
            tortue.forward(1)
    screen.update()


turtle.done()