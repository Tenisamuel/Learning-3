#The following program runs correctly most of the time,but gives a runtime error when certain test data is used.
#Program name: Challenge 101 Example of a runtime error 
powerGenerated = float(input("Total wind power generated week 1 in kwh: "))
daysLowWind = int(input("Number of days with wind below 20mph: "))
dayswithWind = 7 - daysLowWind
averagepower = powerGenerated/dayswithWind
print("Average power generated on windy days:", averagepower)

#Enter and run the program with test data. identify two sets of test data that give different types of runtime error
#when the program is executed.
