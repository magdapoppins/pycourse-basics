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

# a^2 + b^2 = c^2
# a^2 + b^2 = 200^2 = 40 000
a = math.sqrt(20000)

print("{}^2 + {}^2 = {}^2".format(a, a, d))

betsy.circle(r)
# hypo
betsy.left(90)
betsy.forward(d)
# adj
betsy.left(180-45)
betsy.forward(a)
# adj2
betsy.left(90)
betsy.forward(a)
