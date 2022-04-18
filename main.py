import random
import turtle
from turtle import Turtle, Screen
import random

t = Turtle()

turtle.colormode(255)

t.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple

def draw_spirograph(size_the_gap):
    for _ in range(int(360 / size_the_gap)):
        t.color(random_color())
        t.circle(100)
        current_heading = t.heading()
        t.setheading(current_heading +size_the_gap)
        t.circle(100)
draw_spirograph(4)




screen = Screen()
screen.exitonclick()