from turtle import Turtle, Screen, circle
#from turtle import *
#import turtle as t
from numpy import square
import heroes
import random

edi = Turtle()
edi.shape("arrow")
edi.color("blue")


def make_figure(sides):
    size = 100
    angle = 360
    for i in range(sides):
        edi.forward(size)
        edi.right(angle/sides)

# Print Figure
for i in range(3,11):
    colors = ["blue", "red", "yellow", "green", "black", "brown", "purple", "orange", "wheat", "SlateGray", "SeaGreen"]
    edi.color(random.choice(colors))
    make_figure(i)

screen = Screen()
screen.exitonclick()



# 360 / 4 = 90
# 360/ 5 = 72