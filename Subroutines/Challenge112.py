#Program name: Level 7  Challenge 112 area of square, circle or triangle incomplete
# calls functions to calculate area of square, circle or triangle

#Import Python module
....................

def square(side):
    area = side * side
    return .................

def circle(radius):
    area = math.pi * radius**2
    return ............

#function to find area of triangle
def triangle(........................)
    ................................
    .................

#main program
print("This program calculates the area of a square, circle or triangle\n")
myShape = input("Enter a shape, S for square, C for circle, T for triangle: ")
shape = myShape.upper()

#keep asking user to enter shape while it is not S, C or T 
while ..................................................


#user can enter either upper- or lowercase s, c or t
    myShape = input("Please enter S, C or T: ")

#ensure user entry is uppercase by converting entry to uppercase
    shape = myShape.upper()
    
# enter side or radius
if shape == "S":
    sideLength = float(input("Enter length of side: "))
    area = square(sideLength)
................
    circleRadius = float(input("Enter radius: "))
    area = circle(circleRadius)
..............
    triangleBase = ..........................
    triangleHeight = ........................
    area = ..................................

print("Area =",area)
                    
