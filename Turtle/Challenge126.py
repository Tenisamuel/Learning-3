#A list of pen colours may be saved in a list with a statement such as 
#Import the random  module and use the random.randint()function to generate a random number between 0 and 5
#to store in a variable named index.Draw a square with sides of length 100 pixels where each side is a 
#random colour from the list.

import random
import turtle


colour = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)

index = random.randint(0,5)
print("f random index chosen: {index}:")

for i in range(4):
    pen.color(colour[index])
    pen.forward(100)
    pen.left(90)
    index = (index +1) % len(colour)

pen.hideturtle()

screen.exitonclick()