from turtle import Turtle,Screen
tim = Turtle()

screen = Screen()
def move_forward():
    tim.forward(100)
def move_backward():
    tim.backward(100)
def turn_left():
    new_heading = tim.heading() + 100
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 100
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()

# when u press the space tab, the turtle moves forward
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
clear()