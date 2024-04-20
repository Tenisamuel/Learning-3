#write a program to ask a user which times table they would like to see displayed.
#Display the times table from 2 to 12.
# Write the program to collect two input of numbers and it will print the multiplication  
#table of the two input from 2 to 15 

Timetables = int(input("Which times table would you like to be displayed: \n"))

print("\n\nThe Multiplication table of", Timetables, "is given below")

for i in range(2,13):
    result = Timetables * i
    print(Timetables, "x", i, " =", result)

# i = [2,3,4,5,6,7,8,9,10,11,12]