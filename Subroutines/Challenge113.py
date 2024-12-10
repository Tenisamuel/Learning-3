#Program name: Level 7 Challenge 113 menu subroutine with validation completed
#Add the code to validate the coice within the function menu().

def displayRules():
    print("\n********** Option to display rules chosen************\n")

def newGame():
    print("\n********** Option to start new game chosen************\n")

    
def menu():
    print("Menu options")
    print("1. Display rules")
    print("2. Start a new game")
    print("3. Quit")
    choice = input("Enter choice: ")

    #validate chosen option
    while ..........................
        print("\nInvalid option, please enter a number between 1 and 3")
        choice = input("Enter choice: ")

    return choice

#main program
#initialise option to a blank
option = ""
while option != "3":
    option = menu()

#call appropriate function
    if option == "1":
        displayRules()
    elif option == "2":
        ......................
    elif ...................
        print("\nGoodbye!")


    
