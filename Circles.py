import turtle
from itertools import cycle

colors = cycle(['pink', 'yellow', 'green', 'red', 'blue', 'cyan'])


def draw_circle(size, angle, turn, form):
    turtle.pencolor(next(colors))

    if form == "circle":
        turtle.circle(size)
        next_form = 'square'
    elif form == "square":
        for i in range(4):
            turtle.forward(size*2)
            turtle.left(90)
        next_form = 'circle'    
        
    turtle.right(angle)
    turtle.forward(turn)
    draw_circle(size+5, angle+1, turn+1, next_form)

turtle.bgcolor('black')
turtle.pensize(5)
draw_circle(30, 0, 1, 'circle')

