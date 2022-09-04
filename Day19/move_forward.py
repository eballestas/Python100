from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
