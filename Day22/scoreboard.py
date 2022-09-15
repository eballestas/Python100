from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.L_SIDE_SCORE = -70, 170
        self.R_SIDE_SCORE = 70, 170
        self.FONT_SETTINGS = ("Courier", 80, "normal")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.L_SIDE_SCORE)
        self.write(self.l_score, align="center", font=self.FONT_SETTINGS)
        self.goto(self.R_SIDE_SCORE)
        self.write(self.r_score, align="center", font=self.FONT_SETTINGS)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
