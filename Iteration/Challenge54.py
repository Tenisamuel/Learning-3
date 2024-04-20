#write a program to ask a user which times table they would like to see displayed.
#Display the times table from 2 to 12.


Timetables = int(input("Which times table would you like to be displayed: \n"))

print("\n\nThe Multiplication table of", Timetables, "is given below")

for i in range(2,13):
    result = Timetables * i
    print(Timetables, "x", i, " =", result)