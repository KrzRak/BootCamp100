# Import
from turtle import Turtle

# Class
class Scoreboard(Turtle):
    ALIGNMENT = "center"
    FONT = ("Courier", 24, "normal")

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("./023_Snake_HS/data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=self.ALIGNMENT,
            font=self.FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./023_Snake_HS/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
