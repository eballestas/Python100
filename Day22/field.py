from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.pensize(10)
        self.goto(0, 290)
        self.pendown()
        self.setheading(270)
        x = 0
        while x <= 14:
            self.forward(10)
            self.penup()
            self.forward(30)
            self.pendown()
            x += 1
        self.square()

    def square(self):
        self.shape("square")

