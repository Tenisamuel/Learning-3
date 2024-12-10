#Program name: Level 7  Challenge 112 area of square, circle or triangle incomplete
# calls functions to calculate area of square, circle or triangle


#The user must enter the lengths of the base and the height.The formula for the area of a triangle is half
#base times height amend each sub-routine so that it returns the area rounded to two decimal places.

#Import Python module
# import Python() # type: ignore
import math

def square(side):
    area = side * side
    return round(area,3)

def circle(radius):
    area = math.pi * radius**2
    return round(area,3)

#function to find area of triangle
def triangle(base,height):
    area = 1/2 * base * height
    return round(area,3)

#main program
print("This program calculates the area of a square, circle or triangle\n")
myShape = input("Enter a shape, S for square, C for circle, T for triangle: ")
shape = myShape.upper()

#keep asking user to enter shape while it is not S, C or T 
while not (shape == "S" or shape == "C" or shape == "T"):

#user can enter either upper- or lowercase s, c or t
    myShape = input("Please enter S, C or T: ")

#ensure user entry is uppercase by converting entry to uppercase
    shape = myShape.upper()
    
# enter side or radius
if shape == "S":
    sideLength = float(input("Enter length of side: "))
    area = square(sideLength)
elif shape == "C":
    circleRadius = float(input("Enter radius: "))
    area = circle(circleRadius)
else:
    triangleBase = float(input("Enter base length"))
    triangleHeight = float(input("Enter height length"))
    area = triangle(triangleBase,triangleHeight)

print("Area =",area)
                    