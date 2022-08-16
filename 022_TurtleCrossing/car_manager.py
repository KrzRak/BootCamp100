# Import
from turtle import Turtle
import random

# Parameters
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SHAPE = "square"
LEFT = 180

# Class
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape(SHAPE)
        self.setheading(LEFT)
        self.x_pos = 300
        self.y_pos = 0
        self.random_pos()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.move_increment()

    def random_pos(self):
        self.y_pos = random.randint(-250, 250)
        self.goto((self.x_pos, self.y_pos))
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(self.move_speed)

    def move_increment(self):
        self.move_speed += MOVE_INCREMENT
        print(self.move_speed)
