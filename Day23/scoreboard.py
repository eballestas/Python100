from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-250, 250)
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.score}", align="left", font=FONT )

    def add_one(self):
        self.score += 1

