#write a program to ask the user to input two positive integers a and b where a < b. print all the numbers
#between a and b inclusive that are divisible by 13.

type_first_positive_integer_a = int(input("Write the first positive integer:\n"))

type_second_positive_integer_b= int(input("Write the second positive integer:\n"))

print("\n")

for i in range(type_first_positive_integer_a,type_second_positive_integer_b + 1):
    #If the remainder of a dividend is zero, i.e that the dividend is divisible by the divisor.
    if (i % 13 == 0):
        print(i)