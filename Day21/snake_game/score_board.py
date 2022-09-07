from turtle import Turtle
#adding blank comment
FONT = ("Consolas", 24, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def add_one(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=0)
        self.write(f"Game Over" , move=False, align=ALIGNMENT, font=FONT)

