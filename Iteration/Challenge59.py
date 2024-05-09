#write a program that asks the user to enter 5 numbers with decimal points between 1.0 and
#and 10.0. print out how many of the numbers entered are whole numbers


print("This program will write the amount of numbers are integers")

total = 0

for i in range(5):
    num = float(input("Enter 5 numbers "))
    if num == int(num):
        total = total + 1

print("You entered", total , "whole numbers"  )

