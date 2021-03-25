import colorgram
from turtle import Turtle
from turtle import Screen
from random import randint

# extracting colors from the image
colors = colorgram.extract('image.jpg', 40)
collection = []
for x in range(len(colors)):
    color_found = (colors[x].rgb.r, colors[x].rgb.g, colors[x].rgb.b)
    collection.append(color_found)

# print(collection)
# [(227, 230, 236), (243, 236, 242), (244, 239, 226), (235, 243, 239), (194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15), (168, 208, 178), (14, 88, 104), (162, 203, 212), (220, 179, 173), (236, 204, 13)]

# drawing the painting

# setting up the turtle
my_turtle = Turtle()
my_screen = Screen()
Screen().colormode(255)

my_turtle.pensize(20)

# drawing


# project requirements
for x in range(10):
    for _ in range(10):
        (r, g, b) = collection[randint(0, len(collection) - 1)]
        my_turtle.dot(20, (r, g, b))
        my_turtle.penup()
        my_turtle.pensize(15)
        my_turtle.forward(50)
        my_turtle.pensize(20)
        # my_turtle.pendown()
    my_turtle.setposition(0.0, x * 50)
    my_turtle.pendown()

# my_turtle.circle(50)


my_screen.exitonclick()
