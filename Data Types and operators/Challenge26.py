#A taxi company charges basic fee of $5.00 plus $1.30 per km.To estimate the cost of a taxi fare,
#the cab driver inputs the number of km from the airport to a hotel, and the computer caculates and outputs
#the fare.

basic_fee = 5
kilometer = float(input("Enter the distance in kilometers from the airport to hotel: "))

print(kilometer)

fare_price = 1.30 * kilometer + basic_fee

print("The Distance in kilometers from the airport to the hotel is", fare_price)