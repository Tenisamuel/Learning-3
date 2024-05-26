# Write a Python program that asks the user to enter a number and then prints the sum of all numbers from 1 to that number. 
# The program should use a while loop to calculate the sum.

# Example
# Enter a positive integer: 5
# The sum of numbers from 1 to 5 is 15

# In this example, the sum of numbers from 1 to 5 is 
# 1 + 2 + 3 + 4 + 5 = 15

number_written = int(input("Enter a number: \n"))

sum_of_numbers = 1

addednumbers = 0

while sum_of_numbers <= number_written:
    addednumbers = addednumbers + sum_of_numbers
    sum_of_numbers +=1

print("The sum of the number", number_written ,"You have chosen has been summed to be ",addednumbers)