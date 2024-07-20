#A new campervan site near birmingham opened in august.initialise the list as above with an extra row of zeros
#Ask the user to enter the booking figure for august and save the amended two dimensional list.print the amended
#list.


booking = [ [57,68,100,124], [43,52,92,101], [72,78,84,90], [0,0,0,0] ]
siteList = ["Cambridge","Newcastle","Manchester","Oxford"]
monthList = ["May","June","July","August"]

print("Which site do you want to display bookings for?")
site = int(input("Enter 0 for Cambridge, 1 for Newcastle, 2 for Manchester, 3 for Oxford: "))

print("Which month do you want to display bookings for?")
month = int(input("Enter 0 for May, 1 for June, 2 for July, 3 for August: "))

print("Bookings for " + siteList[site] + " in " + monthList[month] + \
      " : " + str(booking[site][month]))  

      