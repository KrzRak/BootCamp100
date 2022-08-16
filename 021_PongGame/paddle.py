from turtle import Turtle
SPEED = 0
COLOR = "white"
SHAPE = "square"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.speed(SPEED)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
