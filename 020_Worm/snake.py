from turtle import Turtle, Screen
import time

MOVE_Distance = 20


class Snake():
    def __init__(self):
        self.length = 3
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, self.length):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto((i * -20, 0))
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, -1, -1):
            if seg == 0:
                self.head.forward(MOVE_Distance)
                continue
            self.segments[seg].goto(self.segments[seg - 1].pos())

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        if self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        if self.head.heading() == 180:
            self.head.left(90)

    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        if self.head.heading() == 270:
            self.head.right(90)

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        if self.head.heading() == 270:
            self.head.left(90)




