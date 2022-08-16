# Import
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Parameters
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = []
scoreboard = Scoreboard()

new_car_time = 7
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

# Main
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car_time += 1

    if new_car_time > 6:
        new_car_time = 0
        car.append(CarManager())

    for car_id in range(0, len(car)):
        car[car_id].move()
        if player.is_on_finish_line():
            scoreboard.increase_score()
            scoreboard.update_scoreboard()
            for car_idx in range(0, len(car)):
                car[car_idx].move_increment()
        if car[car_id].distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            pass

# Visualization exit
screen.exitonclick()
