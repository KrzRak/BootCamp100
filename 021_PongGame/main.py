from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detecting collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Need to bounce
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # Detect when right paddle misses
    if ball.xcor() > 360:
        ball.reset_position()
        score.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -360:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
