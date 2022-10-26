from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=420)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
user_bet = screen.textinput(title="MAKE YOUR BET", prompt="Which turtle will win the race? Enter a color: ")
y = 175
racers = []
for turtle_index in range(0,6):
    turt = Turtle(shape='square')
    turt.penup()
    turt.color(colors[turtle_index])
    turt.goto(x=-240, y=y)
    y-=70
    racers.append(turt)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won. {winner.title()} is the winner!")
            else:
                print(f"You've lost. {winner.title()} is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
