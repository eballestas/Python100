from turtle import Turtle

# adding blank comment
# adding blank comment
FONT = ("Consolas", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score }", move=False, align=ALIGNMENT, font=FONT)

    def add_one(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
