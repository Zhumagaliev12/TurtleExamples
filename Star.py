import turtle

turt = turtle.Turtle()
turt.speed(10)
turt.penup()
turt.goto(-75,0)
turt.pendown()
num = 300
num2 = 120
for i in range(100):
    turt.pensize(2)
    turt.forward(num)
    num1 = num2 - 2
    turt.left(num1)
    num = num - 2
    num1 = num2

turtle.done()
