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

import turtle

def draw_overlapping_circles():
    """
    This function draws five overlapping red circles using the turtle module.
    The turtle cursor is hidden, and the circles are drawn at specific positions.
    """
    turtle.speed(0)  # Set the fastest drawing speed
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.color("red")  # Set the color to red
    turtle.width(2)  # Set the pen width
    
    # Define the positions where circles will be drawn
    positions = [(0, 0), (30, 0), (60, 0), (15, 30), (45, 30)]
    
    for x, y in positions:
        turtle.penup()
        turtle.goto(x, y - 50)  # Move the turtle to starting position
        turtle.pendown()
        turtle.circle(50)  # Draw the circle
    
    turtle.done()  # Keep the window open

# Call the function to draw the circles
draw_overlapping_circles()
