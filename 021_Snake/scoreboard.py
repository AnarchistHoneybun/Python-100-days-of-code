from turtle import Turtle
FONT = ('Courier', 14, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto((0,278))
        self.write(f"Score: {self.score}", move=False, align='center', font=FONT)

    def pointup(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align='center', font=FONT)

    def stop(self):
        self.goto((0,0))
        self.pencolor("red")
        self.write("GAME OVER", move=False, align='center', font=('Courier', 20, 'bold'))