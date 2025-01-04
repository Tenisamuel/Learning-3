#Write a program to generate and print 20 numbers between 30 and 100, rounded to 2 decimal places
#print average of all the numbers rounded to two decimal places.
#
#
total = 0
import random
for i in range(0,20):
    number = float(random.uniform(30,100))
    rounding = round(number, 2)
    print(rounding)
    total += rounding
print("The total amount of numbers are", round(total, 2))
average = total/20
print("The average number here is", round(average, 2))
