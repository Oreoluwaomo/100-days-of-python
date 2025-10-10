from turtle import Turtle,Screen
import random
import turtle
timmy = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color
def draw_spirograph(size_of_gap):

    for _ in range(int(360/ size_of_gap)):
        timmy.speed("fastest")
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)
draw_spirograph(5)


screen = Screen()
screen.exitonclick()