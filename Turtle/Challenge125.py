#Write a program to hide the turtle and position it at coordinates(-200, 100). Then use a for loop
#draw five squares1 each having sides 75 pixels, spaced 20 pixels apart in a horizontal line.

import turtle

turtle.pencolor("green")
turtle.pensize(8)
turtle.setpos(-200,100)
spacing = 20
side_length = 75

def draw_square(side_length):
    for n in range(4):
        turtle.forward(side_length)
        turtle.right(90)
for n in range(5):
    draw_square(side_length)
    turtle.penup()
    turtle.forward(side_length + spacing)
    turtle.pendown()
turtle.hideturtle()