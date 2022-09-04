from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
position = [-90, -60, -20, 20, 60, 90]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=position[turtle_index])

screen.exitonclick()
