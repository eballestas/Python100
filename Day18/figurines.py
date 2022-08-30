from random import randint
from turtle import Turtle, Screen

def brain():
    turtle = Turtle()
    screen = Screen()

    screen.colormode(255)
    sides = 3

    while sides <= 8:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        turtle.pencolor(r, g, b)
        for _ in range(sides):
            turtle.forward(100)
            turtle.right(360 / sides)
        sides += 1

    turtle.forward(200)
    screen.exitonclick()

brain()