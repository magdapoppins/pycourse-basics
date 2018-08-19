# Draw circles with triangles.
import turtle
import math

betsy = turtle.Turtle()

# c = r*pi = d*pi*2
r = 100
d = 2*r
c = d*math.pi 

print("Diameter: ", d)
print("Radius: ", r)

# a^2 * b^2 = c^2
a_sec = (math.sqrt(120))/2
a = a_sec**2

print("{}^2 * {}^2 = {}^2".format(a, a, d))

betsy.circle(r)
betsy.left(90)
betsy.forward(d)
betsy.left(180-45)
betsy.forward(a)
betsy.left(180-45)
betsy.forward(a)
