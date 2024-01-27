#A taxi company charges basic fee of $4.00 plus $0.80 per km.To estimate the cost of a taxi fare,
#the cab driver inputs the number of km from the airport to a hotel, and the computer caculates and outputs
#the fare.

basic_fee = 4

km = float(input("Enter the distance in kilometer from the airport to hotel: "))

print(km)

fareprice = 0.80*km + basic_fee

print("The fare price for this journey is given as: ", fareprice)