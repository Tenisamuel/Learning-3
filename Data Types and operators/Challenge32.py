#Write a program to ask a rocket launch controller to input a number of hours as an integer between 50 and 100
#Convert this to days and hours and print the result in the format:

Num_of_hours = int(input("Enter a number of hours as an integer between 50 and 100: \n"))

time_in_days = Num_of_hours / 24

print("The launch is in:",time_in_days)