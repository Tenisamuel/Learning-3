#Program name Challenge 65 Average runner time

numberOfRrunners = 0
totalTime = 0
moreData = True
print("Enter -1 when no more data")
while moreData:
    runnerName = input("Enter name of runner, xxx to end: ")
    if runnerName != "xxx":
        raceTime = float(input("Enter time for " + runnerName +": "))
        numberOfRrunners = numberOfRrunners + 1
        totalTime = totalTime + raceTime
    else:
        moreData = False
averageTime = totalTime/numberOfRrunners
print("Average race time in seconds:", round(averageTime,2))


# Teni : 36.5 seconds
# Samuel : 38.2 seconds
# Emeka : 39 seconds
# Uche : 41.2 seconds