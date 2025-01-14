#Write a program which sets the pen colour to blue, the width to 5.Draw the following shape on the screen 
#starting at coordinates (-100, -100) (Each square in the drawing is 100*100 pixels).
#
#

#Program name: Challenge 124 draw blue shape
import turtle

#set initial size, colour and position of the pen.
turtle.pensize(5)
turtle.pencolor("blue")
turtle.penup()
turtle.setpos(-100,-100)
turtle.pendown()
turtle.right(180)

#start the drawing
turtle.forward(300)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(300)

turtle.penup()
turtle.setpos(-300,0)
turtle.pendown()

turtle.forward(300)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(300)
