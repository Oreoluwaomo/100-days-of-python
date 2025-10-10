# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r,g,b)
#     rgb_colors.append(new_color)

#extracted the color list after printing the colors
color_list = [(53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35),
 (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109),
 (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143),
 (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]

from turtle import Turtle,Screen
import turtle
import random
turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()