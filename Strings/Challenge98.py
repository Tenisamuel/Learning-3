#The program code for Challenge 98 number incomplete contains the condition
flightNumber = input("Enter flight number AA or BA followed by 4 digits: ")
if not(flightNumber[0:2].upper() == "AA" or 
       flightNumber [0:2].upper() == "BA"):
