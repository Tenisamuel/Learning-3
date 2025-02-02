# Create a list of random numbers and inside the list, count any of the number that has 1 as one entity.
# For example a list of 21,8,56,378,301,88,17,13,61
# The number of "1" that occurs is 5

#random_numbers = ["56","20","43","52","99","50","64","22","18","61","89","77"]

#count = 0

#for i in random_numbers:
#        if "1" in i:
#            count = count + 1


#print("The amount of numbers that have 1 in it are", count)

#import turtle
#window = turtle.screen


#def sum(a, b):
#    total = a + b
#    return total




#two_numbers = int(input("Enter a number"))
#list = []

#for i in range(two_numbers):
#    list1 = list.append(int(input()))

#sum_list1 = 0
#for i in list:
#    sum_list1 = sum_list1 + i



#print("Calculated numbers are", sum_list1)
#first_number = int(input("Enter a number: "))
#second_number = int(input("Enter second number: "))

#calculation = first_number + second_number

#print("This is your two numbers summed together", calculation)


print("This program will either help you multiply,subtract or add")

m_s_a = input("Would you like to multiply,subtract or add\n")

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if m_s_a == "multiply":
    num = number1 * number2
    print(num)
elif m_s_a == "subtract":
    num2 = number1 - number2
    print(num2)
elif m_s_a == "add":
    num3 = number1 + number2
    print(num3)
else:
    print("please satisfy the condition")