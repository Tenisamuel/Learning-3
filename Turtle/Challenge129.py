#Write a statement which calls the function drawpolygon() to draw an equilateral triangle with sides
#of length 100.



#import turtle

#def drawpolygon(numSides, sidelength):
#    interiorAngle = (100 - 2) * 180 /  3
#    turnAngle = 180 - interiorAngle
#drawpolygon()

import turtle

def drawpolygon(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(120)  # Turning left by 120 degrees for an equilateral triangle

drawpolygon(3, 100)  # Draws an equilateral triangle with side length 100

turtle.done()

