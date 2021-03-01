import turtle

t = turtle.Turtle()

symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
t.speed(10)
t.penup()
t.goto(-150, 150)
t.pendown()
t.pensize(2)


def drawBoard():
    for i in range(1, 9):
        if i % 2 == 1:
            for j in range(8):
                if j % 2 == 1:
                    t.begin_fill()
                    drawSquare()
                    t.end_fill()
                else:
                    drawSquare()
        else:
            for j in range(8):
                if j % 2 == 0:
                    t.begin_fill()
                    drawSquare()
                    t.end_fill()
                else:
                    drawSquare()

        t.penup()
        t.goto(-150, (-(i * 50) + 150))
        t.pendown()


def drawSquare():
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)


def writeToBoardSym():
    t.goto(-135, 210)
    t.pendown()
    for i in reversed(symbols):
        t.write(i,font=("Arial", 16, "normal"))
        t.penup()
        t.forward(50)
        t.pendown()
    # t.penup()
    # t.goto(-135, 580)
    # t.pendown()
    # for j in symbols:
    #     t.write(j, font=("Arial", 16, "normal"))
    #     t.penup()
    #     t.forward(50)
    #     t.pendown()

def writeToBoardNum():
    t.penup()
    t.goto(-175, 165)
    t.right(90)
    t.pendown()
    for i in range(1, 9):
        t.write(i, font=("Arial", 16, "normal"))
        t.penup()
        t.forward(50)
        t.pendown()
    # t.penup()
    # t.goto(275, 175)
    # t.right(90)
    # t.pendown()
    # for j in range(1,9,-1):
    #     t.write(j, font=("Arial", 16, "normal"))
    #     t.penup()
    #     t.forward(50)
    #     t.pendown()



drawBoard()
t.penup()
writeToBoardSym()
writeToBoardNum()

turtle.done()
