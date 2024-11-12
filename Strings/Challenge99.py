#Program name: Level 6 Challenge 99 Event catering incomplete
#The program calculates the catering requirements for an event
#Complete the program  Challenge 99 Event catering incomplete, which calculates the catering requirements
#For an event.Ask the user to enter the numbers of guests invited.Validate the entry to ensure the number is numeric
#and in range of 1-75.if it is not, keep asking the user to re-enter until they enter a valid number.Then calculate 
#and print the total requirements based on 8 party snacks per head.



guests = input("Enter number of guests invited (between 1 and 75): ")
validInteger = False


while not validInteger:

    #use the isnumeric(<string>) method to check that entry is numeric
    #before attempting to convert it to an integer
    if not guests.isnumeric():
        print ("This is not a valid number - please re-enter")
        guests = input("Please enter a number between 1 and 75: ")

    #entry is numeric so convert to integer
    else:
        numGuests = int(guests)

        #and check that it is between 1 and 75
        if numGuests in range(1,76):
            validInteger = True
            
            #calculate and print the catering requirements for event
            #based on eight canapes per guest
            print("Canapes required: "+ str(numGuests) * 8)

        else:
            input("Invalid number re enter:")

            #number entered not between 1 and 75, so ask user to re-enter
