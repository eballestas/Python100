from turtle import Turtle, Screen
from random import choice

turtle = Turtle()

angles = [0, 90, 180, 270]
colors = ["orange", "chartreuse", "crimson", "steel blue"]


def random_walk(angles, colors):
    turtle.speed('fast')
    turtle.pensize(10)
    x = True

    while x:
        turtle.pencolor(choice(colors))
        turtle.right(choice(angles))
        turtle.forward(50)
    screen = Screen()
    screen.exitonclick()


random_walk(angles, colors)
