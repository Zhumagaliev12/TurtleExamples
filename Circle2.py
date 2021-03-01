import turtle
import random
import randomcolor

t = turtle.Turtle()

t.speed(10)
t.pensize(3)
for i in range(100):
    col = randomcolor.RandomColor()

    # col = "#"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    t.color(col.generate())
    t.forward(300)
    t.left(110)
t.hideturtle()
turtle.done()