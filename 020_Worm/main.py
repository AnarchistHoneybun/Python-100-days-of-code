from turtle import Turtle, Screen
import time
from snake import Snake


def close():
    screen.bye()


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(close, "c")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
