import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
screen.onkey(turtle.go_up, "Up")

car_list = []

for x in range(4):
    x = CarManager()
    car_list.append(x)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    x.keep_walking()
