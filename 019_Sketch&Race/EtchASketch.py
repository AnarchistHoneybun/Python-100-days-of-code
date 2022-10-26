from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)

def fwd():
    tim.forward(5)
def bck():
    tim.back(5)
def left():
    tim.left(5)
def right():
    tim.right(5)
def clear():
    tim.reset()



screen.listen()
screen.onkeypress(fun=fwd, key="w")
screen.onkeypress(fun=bck, key="s")
screen.onkeypress(fun=left, key="a")
screen.onkeypress(fun=right, key="d")
screen.onkeypress(fun=clear, key="c")

screen.exitonclick()
