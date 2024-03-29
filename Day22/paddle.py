from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.color("White")
        self.goto(location)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
