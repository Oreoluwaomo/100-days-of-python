from turtle import Turtle,Screen
import random
import turtle

timmy = Turtle()
# use  colour
colors = ["red", "orange", "yellow", "green", "blue",
          "purple", "pink", "cyan", "magenta","tomato", "gold",
          "limegreen", "deepskyblue",
          "orchid", "hotpink", "turquoise", "slateblue", "coral", "mediumseagreen"]



#to get angle
def draw_shapes(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range (num_of_sides):
        timmy.forward(100)
        timmy.right(angle)
for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shapes(shape_side_n)


screen = Screen()
screen.exitonclick()
