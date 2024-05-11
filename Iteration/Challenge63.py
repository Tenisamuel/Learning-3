#Enter the program in Example 6, using the same test data.Use the round() function to round averageLengths
#to 1 decimal place Save and execute your program.

day = 0 
totallengths = 0
lengths = int(input("Enter number of lengths: "))

while lengths != -1:
    day = day + 1
    totallengths = totallengths + lengths
    lengths = int(input("Enter number of lengths, -1 to end: "))
averagelengths = totallengths / day
print("Average daily number of lengths:", averagelengths)
x = round(averagelengths, 1)
print("The average lengths have been printed")