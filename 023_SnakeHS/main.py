# Import
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

# Class
class Game:
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.key_setup()

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)

    def key_setup(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def detect_collision_with_food(self):
        if self.snake.head.distance(self.food) < 15:
            self.food.refresh()
            self.snake.extend()
            self.scoreboard.increase_score()

    def detect_collision_with_wall(self):
        if (
            self.snake.head.xcor() > 280
            or self.snake.head.xcor() < -280
            or self.snake.head.ycor() > 280
            or self.snake.head.ycor() < -280
        ):
            self.scoreboard.reset()
            self.snake.reset()

    def detect_collision_with_tail(self):
        for segment in self.snake.segments:
            if segment == self.snake.head:
                pass
            elif self.snake.head.distance(segment) < 10:
                self.scoreboard.reset()
                self.snake.reset()

    def run(self):
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            self.detect_collision_with_food()
            self.detect_collision_with_wall()
            self.detect_collision_with_tail()

        self.screen.exitonclick()

# Main
def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
