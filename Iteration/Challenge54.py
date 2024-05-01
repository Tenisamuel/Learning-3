#write a program to ask a user which times table they would like to see displayed.
#Display the times table from 2 to 12.
# Write the program to collect two input of numbers and it will print the multiplication  
#table of the two input from 2 to 15  2,19

Timetables = int(input("Which times table would you like to be displayed: \n"))

Timetables_two = int(input("Write another times table you want to be displayed: \n"))

print("\n\nThe Multiplication table of", Timetables, "is given below")


for i in range(2,19):
    result = Timetables * i
    print(Timetables, "x", i, " =", result)

print("\n\nThe Multiplication table of",Timetables_two, "is given below")

for i in range(2,19):
    result_two = Timetables_two * i
    print(Timetables_two, "x", i, " =", result_two)



# i = [2,3,4,5,6,7,8,9,10,11,12]