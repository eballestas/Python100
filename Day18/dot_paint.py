# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('picture.jpg', 6)
# rgb_list = []
#
# for _ in colors:
#     r = _.rgb[0]
#     g = _.rgb[1]
#     b = _.rgb[2]
#     value = (r, g, b)
#     rgb_list.append(value)
#
# print(rgb_list)
#
import turtle

color_list = [(249, 248, 248), (229, 236, 245), (239, 246, 242), (246, 236, 240), (132, 164, 203), (227, 149, 99)]

from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
x = -250
y = -250
turtle.colormode(255)
screen.setup(width=700, height=600, startx=None, starty=None)
timmy.penup()
for _ in range(10):
    timmy.goto(x, y)
    for x in range(10):
        timmy.pencolor(choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(20)
        timmy.penup()
    x = -250
    y += 50

screen.exitonclick()
