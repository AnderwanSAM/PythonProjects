import time
from turtle import Turtle, Screen
from Snake_game_GUI_OOP_python.food import Food
from Snake_game_GUI_OOP_python.scoreboard import Scoreboard
from snake import Snake

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating the objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# game On !


game_on = True
screen.listen()
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect when the snake eats the food
    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.increase()
        snake.grow()
    # detect when the snake collided with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.stop_game()
    # detect collision with the tail of the snake
    for x in range(len(snake.segments) - 1):
        if snake.head.distance(snake.segments[x + 1]) < 10:
            game_on = False
            scoreboard.stop_game()

screen.exitonclick()
