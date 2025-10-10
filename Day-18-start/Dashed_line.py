import turtle
from turtle import Turtle,Screen
timmy = Turtle()
for _ in range (5):
    timmy.forward(15)
    timmy.penup()
    timmy.forward(15)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
