#copy the program given in Example 1. Then change the pen colour to green ,pen width

import turtle

turtle.pensize(10)
turtle.pencolor("red")
turtle.setpos(-100,200)
for n in range(6):
    turtle.forward(60)
    turtle.right(60)


