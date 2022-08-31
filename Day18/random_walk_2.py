import turtle
from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
turtle.colormode(255)
angles = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_walk(angle):
    timmy.speed('fast')
    timmy.pensize(10)
    x = True

    while x:
        random_color_choosen = random_color()
        timmy.color(random_color_choosen)
        timmy.right(choice(angle))
        timmy.forward(50)

random_walk(angles)

screen = Screen()
screen.exitonclick()
