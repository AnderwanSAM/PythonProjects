from random import randint
from turtle import Turtle, Screen

# setting up the screen
screen = Screen()
screen.setup(width=700, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the game? Enter its color: ")

# turtles  instances
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []
for color in colors:
    a_turtle = Turtle(shape="turtle")
    a_turtle.color(color)  # giving the turtle a color
    a_turtle.speed(randint(1, 10))  # giving the turtle a random speed
    turtles_list.append(a_turtle)

# put the turtles to the starting line
y_value = -100

for x in range(len(turtles_list)):
    turtles_list[x].penup()
    turtles_list[x].goto(x=-250, y=y_value + (x * 50))


# defining a function to keep track of the evolution of the race and a another one to check the winner
# the finish line is set to be at (x = 100)

def the_race_is_on(list_of_participants):
    # check if all the participants haven't yet reached the finish line
    for index in range(len(list_of_participants)):
        (x_pos, y_pos) = list_of_participants[index].pos()
        if x_pos == 100:  # someone reached the finish line
            return False
    return True


def find_the_winner(list_of_participants):
    for index in range(len(list_of_participants)):
        (x_pos, y_pos) = list_of_participants[index].pos()
        if x_pos == 100:  # someone reached the finish line
            return index


# start the race

while the_race_is_on(turtles_list):
    for index_of_list in range(len(turtles_list)):
        turtles_list[index_of_list].forward(10)

# get the winner and compare with user_bet
winner_index = find_the_winner(turtles_list)
winner_color = turtles_list[winner_index].pencolor()
if user_bet == turtles_list[winner_index].pencolor():
    print(f"Congratulations! You have won ! The winner is the  {winner_color} turtle")
else :
    print(f"Glad You  did not bet money ! You lost. The winner is the {winner_color} turtle ")


screen.exitonclick()
