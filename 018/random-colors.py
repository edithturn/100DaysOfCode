from turtle import Turtle, Screen, circle
#from turtle import *
import turtle as t
from numpy import angle, square
import heroes
import random

edi = Turtle()
edi.shape("arrow")
edi.pensize(5)
edi.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)

    return random_color

def random_walk():
    angles = [0, 90, 180, 270]
    num = random.choice(angles)
    edi.setheading(num)
    edi.forward(20)

def make_walk():
    for i in range(100):
        edi.color(random_color())
        random_walk()

make_walk()

screen = Screen()
screen.exitonclick()



# 360 / 4 = 90
# 360/ 5 = 72