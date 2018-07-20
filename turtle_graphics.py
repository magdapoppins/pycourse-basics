import turtle as t

def draw_rectangle(hor, ver, col):
    t.pendown()
    t.pensize(2)
    t.color(col)
    t.begin_fill()
    for counter in range (1, 3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)

    t.end_fill()
    t.penup()

draw_rectangle(100,100,"red")    
