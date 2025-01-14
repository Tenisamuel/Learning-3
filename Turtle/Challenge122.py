#Write a program which sets the pen width to 3 and pen colour to red. Hide the turtle and draw a pentagon with 
#of length 100 pixels, starting in the middle of the screen.

import turtle

turtle.width(3)
turtle.pensize(10)
turtle.pencolor("red")
for i in range (5):
    turtle.left(72)
    turtle.forward(90)

turtle.hideturtle()

