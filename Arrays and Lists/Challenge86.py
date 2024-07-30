#Program name: Level 5 Challenge 86 Lion cubs incomplete
#Program calculates total number of lion cubs born to three lionesses
#during 2019 and 2020

#name is a list of 3 elements, initialised with the names of the three lions
#the first name is referred to as name[0], the second name as name[1], etc

name = ["Tatiana","Sabrina","Luna"]

#initialise integer variable totalCubs to zero
totalcubs = 0

#ask user to input data for two years, 2019 and 2020
for year in range (2019,2021):
    #print a blank line
    print("\n")
    for lioness in range (3):
        cubs = int(input("Enter number of cubs born to " + name[lioness]\
                         + " in " + str(year) + ": "))

        #add to cumulative total
        totalcubs = totalcubs + cubs


print("Total cubs born:", totalcubs)
      
# This piece of code is trying to make a prompt to carry outthe number of cubs born in 3 years