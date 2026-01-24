import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(10)
t.penup()

def draw_square():
    for i in range(4):
        t.forward(50)
        t.left(90)


def random_colour():
    return random.choice(["red", "green", "blue", "brown", "pink", "black", "purple", "yellow"])


for i in range (20):
    x = random.randint(-200,200)
    y = random.randint(-200,200)

t.color(random_colour())

t.goto(x,y)

t.pendown()
draw_square()
t.penup()

t.hideturtle()