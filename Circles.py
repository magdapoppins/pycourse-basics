import turtle
from itertools import cycle

colors = cycle(['pink', 'yellow', 'green', 'red', 'blue', 'cyan'])


def draw_circle(size, angle, turn):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(turn)
    draw_circle(size+5, angle+1, turn+1)

turtle.bgcolor('black')
turtle.pensize(5)
draw_circle(30, 0, 1)

