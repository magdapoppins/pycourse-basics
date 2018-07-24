import turtle
import math

bob = turtle.Turtle()
# colors can be set in hex values, too
# https://www.w3schools.com/colors/colors_picker.asp

# square
#bob.color("blue")
#for i in range(0, 4):
#    bob.forward(100)
#    bob.right(90)

#bob.penup()
#bob.left(90)
#bob.forward(100)
#bob.pendown()

# triangle
# the first color param is the outline, second is the fill
#bob.color("red", "pink")
#bob.begin_fill()
#for i in range(0,3):
 #   bob.forward(100)
  #  bob.right(120)
#bob.end_fill()    

#bob.penup()
#bob.left(90)
#bob.forward(100)
#bob.pendown()

# hexagon
#bob.color("green")
#for i in range(0, 6):
 #   bob.forward(100)
  #  bob.right(60)

#bob.penup()
#bob.left(90)
#bob.forward(100)
#bob.pendown()    

# flower
#bob.color("cyan")
#for i in range(1, 50):
 #   bob.forward(100)
  #  bob.right(170)

# square roots
#bob.penup()
#bob.left(90)
#bob.forward(100)
#bob.pendown()

#bob.color("red")
#bob.speed(10)
#for i in range(20, 8000, 100):
#    bob.forward(math.sqrt(i))
#    bob.right(90)

bob.color("blue")
for i in range(100):
    bob.forward(math.sqrt(i)*10)
    bob.right(i%90)

# always end these files like this...
turtle.done()
