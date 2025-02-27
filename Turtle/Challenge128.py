#the statement turtle.circle(50) drwas a circle of radius of radius 50. Write a program to hide the turtle
#and draw five overlapping red circle of raidus.

import turtle

def draw_overlapping_circles():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color("red")
    turtle.width()

    positions = [(0,0), (30,0), (60,0), (15,30), ]
    for x,y in positions:
        turtle.penup()
        turtle.goto(x, y - 50)
        turtle.pendown()
        turtle.circle(50)
    turtle.down()

draw_overlapping_circles()
