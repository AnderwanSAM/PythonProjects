from turtle import Turtle, Screen
from random import randint

junior_turtle = Turtle()
junior_turtle.shape("turtle")
junior_turtle.color("black")
screen = Screen()

junior_turtle.speed(10)
# challenge 1 : Draw a square
junior_turtle.penup()
junior_turtle.sety(300)
junior_turtle.pendown()
for x in range(4):
    junior_turtle.forward(100)
    junior_turtle.right(90)

# challenge 2 :  Draw a dash line

# go to a new position to draw
junior_turtle.right(90)
junior_turtle.penup()
junior_turtle.forward(300)
junior_turtle.pendown()
# draw the dash line
junior_turtle.shape("arrow")
junior_turtle.left(90)
for x in range(15):
    junior_turtle.forward(10)
    junior_turtle.penup()
    junior_turtle.forward(10)
    junior_turtle.pendown()

# challenge 3 : Multiples shapes

screen.clear()
junior_turtle2 = Turtle()
junior_turtle2.speed(10)
# get into suitable position
junior_turtle2.penup()
junior_turtle2.sety(250)
junior_turtle2.setx(-50)
junior_turtle2.pendown()
# create a list for the colors
colours = ["green", "red", "yellow", "black", "maroon", "purple", "blue", "gray", "CornflowerBlue", "DarkOrchid",
           "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(sides):
    # deduce data from sides number
    angle = 360 / sides
    current_color = colours[3 - sides]
    for _ in range(sides):
        junior_turtle2.color(current_color)  # set the color
        junior_turtle2.forward(50)
        junior_turtle2.right(angle)


for x in range(8):
    draw_shape(x + 3)


# challenge 4 : RandomWalk

#  clear the screen
screen.clear()
# new Turtle
del junior_turtle
del junior_turtle2
junior_turtle = Turtle()
junior_turtle.hideturtle()
junior_turtle.pensize(10)
junior_turtle.speed(10)
for _ in range(50):
    junior_turtle.color(colours[randint(0, len(colours) - 1)])  # set th turtle with  a random colour
    toss = randint(0, 1)
    if toss == 0:
        junior_turtle.left(90)
    else:
        junior_turtle.right(90)
    junior_turtle.forward(15)

# challenge 5  : Drawing a sirograph
screen.clear()
del junior_turtle
junior_turtle = Turtle()
junior_turtle.speed(10)

for x in range(25) :
    junior_turtle.color(colours[randint(0, len(colours)-1)])
    junior_turtle.circle(50)
    junior_turtle.left(x+10)

screen.exitonclick()
