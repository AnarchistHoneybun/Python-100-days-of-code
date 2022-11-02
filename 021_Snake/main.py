from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def close():
    screen.bye()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.colormode(255)
screen.tracer(0)
screen.title("My Snake Game")

food = Food()
snake = Snake()
scoreboard = ScoreBoard()

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
    # food collision detection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.elongate()
        scoreboard.pointup()

    # detect wall collision

    if snake.head.xcor() >= 280 or snake.head.xcor() <= -285 or snake.head.ycor() >= 300 or snake.head.ycor() <= -280:
        snake.stop()
        scoreboard.stop()
        food.stop()
        screen.update()
        game_on = False

    # detect self collision

    for i in range(4, snake.length):
        if snake.head.distance(snake.segments[i]) < 20:
            snake.stop()
            scoreboard.stop()
            food.stop()
            screen.update()
            game_on = False
screen.exitonclick()
