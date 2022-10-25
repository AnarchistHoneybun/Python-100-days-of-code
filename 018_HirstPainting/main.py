from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 10)
palette = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_col = (r, g, b)
    palette.append(new_col)

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape('circle')
screen.screensize(300,300)
tim.penup()
x = -135
y = -135
tim.goto(x,y)
tim.pendown()
for i in range(20):
    for j in range (20):
        tim.color(random.choice(palette))
        tim.pendown()
        tim.dot(10)
        x+=15
        tim.penup()
        tim.goto(x,y)
    tim.penup()
    x = -135
    y += 15
    tim.goto(x,y)



screen.exitonclick()