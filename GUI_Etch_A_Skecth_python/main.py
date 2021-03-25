from turtle import Turtle, Screen

# instances
my_turtle = Turtle()
screen = Screen()


# moving functions
def move_forward():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.left(180)
    my_turtle.forward(10)


def counter_clockwise():
    my_turtle.left(180)


def clock_wise():
    my_turtle.right(180)


def clear_drawing():
    screen.clear()


def go_up():
    my_turtle.left(45)


def go_down():
    my_turtle.right(45)


screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="C", fun=clear_drawing)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clock_wise)
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="Down", fun=go_down)


screen.exitonclick()
