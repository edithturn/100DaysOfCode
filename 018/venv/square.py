from turtle import Turtle, Screen, circle
#from turtle import *
#import turtle as t
from numpy import square
import heroes

edi = Turtle()
edi.shape("turtle")
edi.color("blue")

square_sides = 4
for i in range(square_sides):
    edi.right(90)
    edi.forward(100)

screen = Screen()
screen.exitonclick()

print(heroes.gen())