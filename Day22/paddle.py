from turtle import Turtle


class Paddle:
    def __init__(self, location):
        super().__init__()
        self.paddle = Turtle("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.speed("fastest")
        self.paddle.penup()
        self.paddle.color("White")
        self.paddle.goto(location, 0)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
