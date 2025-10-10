from turtle import Turtle,Screen
import random
timmy = Turtle()
colors = ["tomato", "gold", "limegreen", "deepskyblue", "orchid", "red",
          "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta",
          "hotpink", "turquoise", "slateblue", "coral", "mediumseagreen"]
directions = [0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
