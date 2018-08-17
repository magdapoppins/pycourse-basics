import turtle

turtle.bgcolor('black')
turtle.speed('fast')

betsy = turtle.Turtle()

betsy.pencolor('pink')
betsy.pensize(0.5)


#for i in range(40):
#    betsy.circle(50)
#    betsy.right(10)
#    betsy.forward(20)


#    for i in range(6):
#        betsy.forward(130)
#        betsy.right(60)
#    betsy.right(10)

#for i in range(50):
#    for i in range(4):
#        betsy.forward(100)
#        betsy.right(90)
#    betsy.right(10)
#    betsy.forward(15)

        
for i in range(50):
    for i in range(4):
        betsy.forward(200)
        betsy.right(90)
    betsy.right(20)
    betsy.forward(15)
