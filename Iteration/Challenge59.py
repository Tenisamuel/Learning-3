#write a program that asks the user to enter 5 numbers with decimal points between 1.0 and
#and 10.0. print out how many of the numbers entered are whole numbers


print("Enter five numbers with or without decimal points")
print("The program prints how many were whole numbers\n")

total = 0

for n in range(5):
    num = float(input("Enter number: "))
    if num == int(num):
        total = total + 1
print("You entered",total,"whole numbers")
