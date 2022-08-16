# Issue with Tkinter
# /bin/python3 /home/dzyniu/VSCode/Phyton/BootCamp100/018_start_turtle/main.py
# Traceback (most recent call last):
#   File "/home/dzyniu/VSCode/Phyton/BootCamp100/018_start_turtle/main.py", line 1, in <module>
#     import turtle as t
#   File "/usr/lib/python3.10/turtle.py", line 107, in <module>
#     import tkinter as TK

# Solution
# sudo apt-get install python3.10-tk


# Import
import turtle as t
import random

# Parameters
tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Parameters for turle
tim.pensize(1)
tim.speed(0)

# Make a circle
for _ in range(100):
    tim.pencolor(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)

# Make a multiple circles
while True:
    #tim.pencolor(random.choice(colours))
    tim.pencolor(random_color())
    tim.setheading(random.randrange(0, 360, 90))
    tim.forward(30)
