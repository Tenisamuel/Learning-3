#write a program that asks an employee to enter thier overtime hours each day of the week to the nearest
#quater hour, e.g, 1.25. The total overtime over the week is caculated and printed at the end of the 
#program

print("overtime calculator\n")
print("Enter your overtime hours for Monday-Friday (day 1 to day 5)\
\nto the nearest quarter hour, e.g. 1.25\n")
total = 0

for day in range(1,6):
    hours = float(input("Enter overtime worked on day " + str(day) + " in hours: "))
    total = total + hours

print("\nYou worked",total,"overtime hours this week.")