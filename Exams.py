#array months[12]
#months = ["January","Febuary","March","April","May","June","July","August","September","October","november","December"]
#array rainfall = 0
#for i = 0 to month.length-1
#       rainfall[i] = int(input("Please input rainfall for month", months[i]))
#       annualrainfall = annualrainfall + rainfall[i]
#next i
#aveargerainfall = annualrainfall/12
#monthsaboveaverage = 0
#for i = 0 to month.length-1
#    if rainfall[i]>averagerainfall then
#       monthsaboveaverage = monthsaboveaverage+1
#    endif
#   print(months[i] + ": " + str(rainfall[i]))
#next i
#print(annualrainfall)
#print(aveargerainfall)
#print(monthsaboveaverage)

#months = ["January","Febuary","March","April","May","june","july","august","september","october","november","December"]
#rainfall_list = []
#annualrainfall = 0
#for i in range(len(months)-1):
#    print("Insert the input rainfall for the month of", months[i])
#    rainfall = int(input("Please input rainfall in the last month"))
#    rainfall_list.append(rainfall)
#    annualrainfall = annualrainfall + rainfall
#averagerainfall = annualrainfall / 12
#monthsaboveaverage = 0
#for i in range(len(months)-1):
#    if rainfall_list[i] > averagerainfall:
#        monthindicate = []
#        monthindicate.append(rainfall_list[i])
#        monthsaboveaverage = monthsaboveaverage + 1
#    print(months[i] + ": " + str(rainfall_list[i]))
#print(annualrainfall)
#print(averagerainfall)
#print(monthsaboveaverage)
#print("These are the months above average", monthindicate)

#marksFile = open("exams.txt", 'w')
#for n in range (20):
#    name = input("Enter student name: ")
#    mark = input("Enter student mark: ")
#    marksFile.write(name + "," + mark + "\n")
#marksFile.close()

with open("exams.txt", "r") as file:
    for line in file:
        line = file.readlines()
        print(line, end = "")
print("End of file reached")
file.close()


