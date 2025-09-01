# import colorgram
#
# colors = colorgram.extract(f="image.jpg", number_of_colors= 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colours = r , g, b
#     rgb_colors.append(colours)
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen
colour_list = [(202, 164, 109), (150, 75, 49), (223, 201, 135), (52, 93, 124),
               (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71),
               (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
               (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50),
               (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129),
               (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
               (174, 94, 97), (176, 192, 209)]

turtle.colormode(255)
e = Turtle()

e.speed("fastest")

smtg = 10


for i in range(10):
    e.setheading(225)
    e.penup()
    e.forward(250)
    e.setheading(0)
    for j in range(10):

        e.penup()
        new_color = random.choice(colour_list)
        e.dot(20, new_color)
        e.forward(50)

    smtg += 30
    e.home()
    e.sety(smtg - 10)

e.hideturtle()
screen = Screen()

screen.exitonclick()


