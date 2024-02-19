import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=800, height=700)
user_bet = screen.textinput(title="Make your Bet.", prompt="Which turtle will win the race? Enter a color (ROYGBIV):  ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]



def init_starting_line(list_of_colors, first_position):
    racers = []
    for i in list_of_colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(i)
        new_turtle.turtlesize(3)
        new_turtle.goto(x=-370, y=first_position)
        first_position += 80
        racers.append(new_turtle)
    return racers

def race(list_of_racers):
    winner = ""
    if user_bet:
        is_race_on = True
    while is_race_on:

        racer = random.choice(list_of_racers)
        racer.forward(random.randint(1, 10))

        if racer.xcor() > 375:
            winner = racer.fillcolor()
            is_race_on = False

    return winner

def check_results(outcome, bet):
    if outcome.lower() == bet.lower():
        print(f"You won the bet, The {outcome} turtle is the winner!")
    else:
        print(f"You lost the bet, The {outcome} turtle is the winner....")

racers = init_starting_line(colors, -250)
winner = race(racers)
check_results(winner, user_bet)

screen.exitonclick()