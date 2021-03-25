from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # moving the snake body

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        #  create a new body part and add it to the body
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(x=self.segments[len(self.segments) - 1].xcor(), y=self.segments[len(self.segments) - 1].ycor())
        self.segments.append(seg)

"""""
class Snake:
    def __init__(self):
        self.positions = [0, -20, 20]
        self.body = []

        for x in range(3):
            a_turtle = Turtle(shape="square")
            a_turtle.color("white")
            a_turtle.penup()
            a_turtle.goto(self.positions[x], 0)
            self.body.append(a_turtle)

    # moving the snake body

    def move_forward(self):
        for index in range(len(self.body) - 1, 0, -1):
            (x_pos, y_pos) = self.body[index - 1].pos()
            self.body[index].goto(x_pos, y_pos)
        self.body[0].forward(20)

    def move_up(self):
        for index in range(len(self.body) - 1, 0, -1):
            (x_pos, y_pos) = self.body[index - 1].pos()
            self.body[index].goto(x_pos, y_pos)
        self.body[0].left(90)
        self.move_forward()

    def turn_left(self):
        for index in range(len(self.body) - 1, 0, -1):
            (x_pos, y_pos) = self.body[index - 1].pos()
            self.body[index].goto(x_pos, y_pos)
        self.body[0].left(90)
        self.move_forward()

    def turn_right(self):
        for index in range(len(self.body) - 1, 0, -1):
            (x_pos, y_pos) = self.body[index - 1].pos()
            self.body[index].goto(x_pos, y_pos)
        self.body[0].right(90)
        self.move_forward()

    def move_down(self):
        for index in range(len(self.body) - 1, 0, -1):
            (x_pos, y_pos) = self.body[index - 1].pos()
            self.body[index].goto(x_pos, y_pos)
        if self.body[0].xcor() < self.body[1].xcor():  # deduce which way the snake is turned to
            self.body[0].left(90)
        else:
            self.body[0].right(90)
        self.move_forward()

"""""