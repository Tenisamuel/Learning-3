#Program name: Level 6 Challenge 94 Flight number incomplete
#Program validates a flight number, 2 letters followed by 4 digits

validNumber = False

while not validNumber:
    validNumber = True
    flightNumber = input("Enter flight number AA or BA followed by 4 digits: ")

    #perform three validation checks
    if not(flightNumber[0:2].upper() == "AA" \
           or ...........................
        validNumber = False
    elif not ..................isdigit()):
        validNumber = False
    #check that length of flight number = 6
    elif ......................    
        validNumber = False

    #if an invalid flight number was entered, print an error message 
    if not .................
        print("Invalid flight number, please re-enter")

#keep looping round until a valid number is entered
#endwhile

print("Flight number accepted:", flightNumber.upper())