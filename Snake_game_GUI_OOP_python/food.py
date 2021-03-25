from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(10)
        self.goto(x=randint(-200, 200), y=randint(-200, 200))
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-200, 200), y=randint(-200, 200))



