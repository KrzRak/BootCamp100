# Import
from turtle import Turtle

# Parameters
SPEED = 1
COLOR = "white"
SHAPE = "circle"
MOVE_DISTANCE = 10

# Class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.speed(SPEED)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.8

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
