import colorgram
import random
import turtle
from turtle import Turtle, Screen

colours = colorgram.extract('hirst.jpg', 30)

def list_of_rgb():

    list_of_tups = []

    length = (len(colours))

    for x in range(length):
        col = colours[x]
        r = col.rgb.r
        g = col.rgb.g
        b = col.rgb.b
        rgb = (r, g, b)
        list_of_tups.append(rgb)

    return list_of_tups


colour_list = list_of_rgb()
print(len(colour_list))

# create the painting

tim = Turtle()
turtle.colormode(255)
screen = Screen()

screen.setup(width=500, height=500)

tim.penup()
tim.goto(-225, -225)
tim.speed('fastest')
tim.hideturtle()

i = 1
for x in range(5):
    while i < 11:
        rand = random.randint(0, 29)
        tim.color(colour_list[rand])
        tim.dot(30)
        tim.penup()
        tim.forward(50)
        print(i)
        i += 1

    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)

    i = 1

    while i < 11:
        rand = random.randint(0, 29)
        tim.color(colour_list[rand])

        tim.dot(30)
        tim.penup()
        tim.forward(50)
        print(i)
        i += 1

    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)
    i = 1


screen.exitonclick()

