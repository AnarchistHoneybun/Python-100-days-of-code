from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.goto((random.randint(-250,250),random.randint(-250,250)))

    def refresh(self):
        self.goto((random.randint(-250, 250), random.randint(-250, 250)))

    def stop(self):
        self.hideturtle()
        self.goto((0,0))