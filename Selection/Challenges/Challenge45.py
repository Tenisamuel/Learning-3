#Write a program to input the length and width of a maze. if the two sides are equal, print"The maze is square"
#.if the sides are not equal, print "The maze is "rectangular". include at least two comments in your program.

#This python statement prompts you to write a value for length and width

length = int(input("Write the length of the maze\n"))

width = int(input("Write the width of the maze\n"))

#This python statement is used to add the values to see if they are equal if yes the maze is square
#if not the maze is rectangular.
if length == width:
    print("The maze is square")

else:
    print("The maze is rectangular")

    