#Program name: Challenge 120 Random number test completed
#The program simulates throwing a 6-sided die
#The user chooses how many times the die will be thrown
#The number of times each face appears is printed at the end of the test

import random

#function menu() called from main program 
def menu():
    print("\nMenu options")
    print("1. Explain the purpose of the test")
    print("2. Start a new test")
    print("3. Quit")
    choice = input("Enter choice: ")

    #validate choice
    while not choice in ["1","2","3"]:
        print("Invalid option, please enter a number between 1 and 3")
        choice = menu()

    #return the user's choice to the main program
    return choice

#procedure displayRules() displays the purpose of the test
#this subroutine has no parameters and returns no value 

def displayRules():
    print("\nThis program simulates the throw of a die, \
and tests the fairness of the random number generator")
    print("\nEach number should appear approximately the same number of times.\n")
    print("For example, if a die is thrown 600 times, \
\neach face should appear approximately 100 times.\n")
    print("The more times a die is thrown, \nthe closer the actual result will be \
to the theoretical probability\n")
         

#procedure testNumbers() carries out the simulation
#this subroutine has no parameters and returns no value 
    
def testNumbers():

    #define a list named face containing 6 zeros in face[0], face[1] to face[6]   
    #face[0] will not be used
    face = [0]*7      
    print("Select one of the numbers 6, 60, 600, 6000") 
    throws = input("How many times do you want to roll the die? ")

    #validate user entry
    while not throws in ["6","60","600","6000"]:
       print("Invalid option, please enter 6, 60, 600 or 6000")   
       throws = input("How many times do you want to roll the die? ")

    #convert throws to integer
    throws = int(throws)
    
    #Carry out the simulation.
    #Throw the dice the selected number of times and print result
    for n in range(throws):
        #generate a random number in the range 1-6
        dieRoll = random.randint(1,6)

        #add 1 to the number of times that face appeared
        face[dieRoll] = face[dieRoll] + 1 

    for dieface in range (1,7):
          print(dieface," was thrown",face[dieface], "times")

def quitProgram(message):
    print(message)

#*****************************************************************
#main program starts here
#*****************************************************************

option = menu()

# perform chosen option

while  option!= "3":
    if option == "1":
        displayRules()

    elif option == "2":        
        testNumbers()

    option = menu()    

#call procedure quitProgram() to quit program, passing a suitable message
quitProgram("Goodbye!")


#end of main program
