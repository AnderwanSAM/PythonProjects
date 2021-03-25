from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.pendown()
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def stop_game(self):
        self.goto(x=0, y=0)
        self.write(f" Game Over. ", align=ALIGNMENT, font=FONT)
