import random
import turtle
colors = ['black','lightpink','red' ,'yellow', 'green','orange']
t = turtle.Turtle()
t.speed(1000)
turtle.bgcolor("aquamarine")
length=600
angle =70
size=3
for i in range(length):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+50)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick()
turtle.bgcolor("black")      