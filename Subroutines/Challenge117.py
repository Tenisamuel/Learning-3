#Load the program Challenge 117 local and global variables from the challenge solutions\ level 7 folder
#Examine the code and run the program

#Name two global variables used in the program.

#Name four local variables used in the function simulation()

#Explain the effect on the execution of the program of uncommenting the statement print(face) in the main 
#Program.



import random
def simulation():
    global title
    title = "Game number 1"
    #define a list named face containing 6 zeros in face[0], face[1] to face[6]   
    #face[0] will not be used
    face = [0]*7
    for n in range(6):
        #generate a random number in the range 1-6
        dieRoll = random.randint(1,6)
        #add 1 to the number of times that face appeared
        face[dieRoll] = face[dieRoll] + 1 
    print(heading)
    for dieface in range(1,7):
          print(dieface," was thrown",face[dieface], "times")

#****************** main program *********************
title = "Game number 1"
print(title)
heading = "Dieroll simulation"
simulation()

#What is the effect of uncommenting the statement below?
#print(face)
