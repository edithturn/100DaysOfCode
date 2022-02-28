from turtle import Turtle, Screen, circle

from numpy import square

edi_the_turtle = Turtle()

edi_the_turtle.shape("turtle")
edi_the_turtle.color("blue")

square_sides = 4
for i in range(square_sides):
    edi_the_turtle.right(90)
    edi_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()