import turtle
import random
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-75,0)
t.pendown()

num1 = 200
for i in range(84):
    t.pensize(2)
    t.forward(num1)
    t.left(90)

    num1 = num1 -5



turtle.done()