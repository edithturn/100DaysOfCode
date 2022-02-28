from turtle import Turtle, Screen, circle
#from turtle import *
#import turtle as t
from numpy import square
import heroes

edi = Turtle()
edi.shape("arrow")
edi.color("blue")


for i in range(80):
    edi.pendown()
    edi.forward(5)
    edi.penup()
    edi.forward(5)

screen = Screen()
screen.exitonclick()

