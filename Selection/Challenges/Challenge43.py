#Write a program to input the left - and right hand weights of a rollercoaster ride car. 
#if the two weights are equal, print "The car is balanced". if the weights are not equal, print 
#"The car is not balanced." include at least two comments in your program.

#This if statement helps to compare two or more things together.
#

left_weights = float(input("What is the weight of the left hand weight?\n"))

right_weights = float(input("What is the weight of the right hand weight?\n"))

if left_weights == right_weights:
    print("The car is balanced")

else:
    print("The car is not balanced")

