# Import
from turtle import Turtle

# Parameters
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)