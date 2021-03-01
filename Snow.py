import turtle

t = turtle.Turtle()
t.speed(10)


def start(x: float):
    """This function clears window and make turtle go to start"""
    t.clear()
    t.penup()
    x = x if x < 0 else -x
    t.goto(x, 0)
    t.pendown()


def curve_minkowski(length: float, iterations: int):
    """This function draw Minkowski's curve"""

    if iterations == 0:
        t.forward(length * 4)
    else:
        curve_minkowski(length/4, iterations - 1)
        t.left(90)
        curve_minkowski(length/4, iterations - 1)
        t.right(90)
        curve_minkowski(length/4, iterations - 1)
        t.right(90)
        curve_minkowski(length/4, iterations - 1)
        curve_minkowski(length/4, iterations - 1)
        t.left(90)
        curve_minkowski(length/4, iterations - 1)
        t.left(90)
        curve_minkowski(length/4, iterations - 1)
        t.right(90)
        curve_minkowski(length/4, iterations - 1)

LENGTH = 100       # длина линии

ITERATION = 3      # номер итерации

start(LENGTH * 2)

curve_minkowski(LENGTH, ITERATION)

turtle.done()    # функция чтобы програма не завершалась сразу
