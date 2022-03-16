from turtle import Turtle, Screen, circle
#from turtle import *
#import turtle as t
from numpy import angle, square
import heroes
import random

edi = Turtle()
edi.shape("arrow")
edi.color("blue")
edi.pensize(5)
edi.speed("fastest")

        
def random_walk():
    angles = [0, 90, 180, 270]
    num = random.choice(angles)
    edi.setheading(num)
    edi.forward(20)

def make_walk():
    for i in range(100):
        colors = ["blue", "red", "yellow", "green", "black", "brown", "purple", "orange", "wheat", "SlateGray", "SeaGreen"]
        edi.color(random.choice(colors))
        random_walk()

make_walk()

screen = Screen()
screen.exitonclick()



# 360 / 4 = 90
# 360/ 5 = 72