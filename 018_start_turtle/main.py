import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.pensize(1)
tim.speed(0)

for _ in range(100):
    tim.pencolor(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)







# while True:
#     #tim.pencolor(random.choice(colours))
#     tim.pencolor(random_color())
#     tim.setheading(random.randrange(0, 360, 90))
#     tim.forward(30)
