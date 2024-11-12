#Program name: Level 6 Challenge 99 Event catering incomplete
#The program calculates the catering requirements for an event

guests = input("Enter number of guests invited (between 1 and 75): ")

..............................

while not validInteger:

    #use the isnumeric(<string>) method to check that entry is numeric
    #before attempting to convert it to an integer
    if .............................
        print ("This is not a valid number - please re-enter")
        guests = input("Please enter a number between 1 and 75: ")

    #entry is numeric so convert to integer
    else:
        numGuests = .......................

        #and check that it is between 1 and 75
        if numGuests in range(1,76):
            validInteger = True
            
            #calculate and print the catering requirements for event
            #based on eight canapes per guest
            print("Canapes required: " + .................)

        else:
        #number entered not between 1 and 75, so ask user to re-enter
        
            ...................................................
