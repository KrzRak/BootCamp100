# Import
from turtle import Turtle

# Parameters
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

# Class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=200)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
