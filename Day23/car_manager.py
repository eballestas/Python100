from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto((250, STARTING_MOVE_DISTANCE - 250))
        self.setheading(180)
        self.shape("square")

    def keep_walking(self):
        self.forward(MOVE_INCREMENT)
