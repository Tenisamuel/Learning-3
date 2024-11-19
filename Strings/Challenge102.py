#write a program that allows a user to enter two numbers area1 and area2. example 2.347 and 1, representing
#average daily rainfall in two different areas.Print a heading,and print the numbers with two decimal places 
#on one line, each in a 10-character space.

area_one = float(input("Enter the average daily rainfall for area 1, Has to be decimal:"))
area_two = int(input("Enter the average daily rainfall for area 2: "))

#Heading
print("{:<10}{:>10}".format("Area1","Area2"))

#Data
print("{:<10}{:>10}".format(area_one,area_two))