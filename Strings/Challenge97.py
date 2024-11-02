#Program name: Level 6 Challenge 94 Flight number incomplete
#Program validates a flight number, 2 letters followed by 4 digits

#Flight numbers are assigned to all journeys by air.in an airport terminal, the user is promted to enter a flight
#code made up of a 2-letter airline code made up of a 2 letter airline code (uppercase) followed by 4 digits.

#The program checks that the airline code is either "AA" or "BA".it then checks the last 4 digits to ensure 
#they are numeric.Lowercase letters are accepted. if the number is not valid, a message "invalid flight number,
#please re-enter"is printed.

#This is reapeated until a valid flight number is entered.A message "Flight number accepted" is Printed.

validNumber = False

while not validNumber:
    validNumber = True
    flightNumber = input("Enter flight number AA or BA followed by 4 digits: ")

    #perform three validation checks
    if not(flightNumber[0:2].upper() == "AA" \
           or flightNumber [0:2].upper() == "BA"):
           validNumber = False
    elif not(flightNumber[2:6].isdigit()):
        validNumber = False
    #check that length of flight number = 6
    elif not (len(flightNumber) == 6):
        validNumber = False

    #if an invalid flight number was entered, print an error message 
    if not validNumber:
        print("Invalid flight number, please re-enter")

#keep looping round until a valid number is entered
#endwhile
#"characters"

print("Flight number accepted:", flightNumber.upper())