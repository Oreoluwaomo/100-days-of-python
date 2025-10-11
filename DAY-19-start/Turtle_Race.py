import turtle
from turtle import Turtle,Screen
import random
is_race_on = False

screen = Screen()
#increase size of screen
screen.setup(500,400)
#pop on screen
user_bet = screen.textinput("Make your bet","Which turtle will win "
                                 "the race? pick a colour: ")
#turtle colors
colors = ["red","green",'yellow',"orange","blue","purple"]
#y position
y_positions = [-70,-40,-10,20,50,80]
# list for all turtles
all_turtles = []
#turtle move the  left edge...start of the line and change the shape,
# create 6 turtles using range
for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
# while race is on
if user_bet:
    is_race_on = True
while is_race_on:
    #distance for turtles
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()