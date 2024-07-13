#Write a program to ask the user which site and which month they would like to have the booking
#displayed for, and display the figure.

booking = [ [57,68,100,124], [43,52,92,101], [72,78,84,90] ]
siteList = ["Cambridge","Newcastle","Manchester"]
monthList = ["May","June","July","August"]

print("Which site do you want to display bookings for?")
site = int(input("Enter 0 for Cambridge, 1 for Newcastle, 2 for Manchester: "))

print("Which month do you want to display bookings for?")
month = int(input("Enter 0 for May, 1 for June, 2 for July, 3 for August: "))

print("Bookings for " + siteList[site] + " in " + monthList[month] + \
      " : " + str(booking[site][month]))  