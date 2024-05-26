# Write a Python program that asks the user to enter a number and then prints the sum of all numbers from 1 to that number. 
# The program should use a while loop to calculate the sum.

# Example
# Enter a positive integer: 5
# The sum of numbers from 1 to 5 is 15

# In this example, the sum of numbers from 1 to 5 is 
# 1 + 2 + 3 + 4 + 5 = 15

number = int(input("Enter an integer number: \n"))

current_number = 1

sum_of_number = 0

while current_number <= number:
    sum_of_number = sum_of_number + current_number
    current_number = current_number + 1

print("The sum of numbers from 1 to", number , "is given as", sum_of_number)