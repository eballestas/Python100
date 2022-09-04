import random
import turtle
from turtle import Turtle, Screen
from random import randint

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
position = [-90, -60, -20, 20, 60, 90]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=position[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You won! the winning turtle is {winning_color}")
            else:
                print(f"You Lost! the winning turtle is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
