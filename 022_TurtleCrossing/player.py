from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 100
FINISH_LINE_Y = 280
COLOR = "black"
SHAPE = "turtle"
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_start()
        self.color(COLOR)
        self.shape(SHAPE)
        self.y_move = MOVE_DISTANCE
        self.setheading(UP)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(x=0, y=new_y)


    def is_on_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.go_to_start()
            return True
        else:
            return False


