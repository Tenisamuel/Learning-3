#A cyclist training for a race records his times over n miles for two consecutive days. His times are 6 hours
#40 minutes and 5 Hours 42 minutes.

#Complete the Python program Challenge 15 average cyclist time incomplete in the Starred challenges
#(incomplete) folder to caculate his average time in minutes, Convert the average to hours and minutes and 

#print the result.


Distance_in_Miles = int(input("Enter the amount of miles you cycled: \n"))
time_hours = int(input("Enter the time in hours: \n"))

time_min = int(input("Enter the time in minutes: \n"))

#convert_hours_to_minutes = (time_hours * 60) + time_min

total_time_in_hours = (time_min / 60) + time_hours

#print("The total time in minutes is given as:", convert_hours_to_minutes,"minutes")

print("The total time in hours is given as", total_time_in_hours , "hours")

#Total_time_in_hours = float(input("Enter the total amount of time in hours: \n"))
#Distance_divide_time = (35 / Total_time_in_hours  )
#print("The total speed the cyclist used in the race is", Distance_divide_time)

speed_of_journey = 35 / total_time_in_hours

print("The speed of the journey is given as:", speed_of_journey , "miles/hr")