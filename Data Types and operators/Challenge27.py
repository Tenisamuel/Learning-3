#The formula for converting a Farenheit temperature (F) to celcius (C) is
#                 C =(F - 32) * 5/9

#Write a program to allow a user to enter a Farenheit temperature, convert the temperature to celcius
#and print out the result of the conversation.Test your program four times, entering tempratures of 212, 89.5
#32, -40 At what temperature are the farenheit and celcius temperatures the same value?


valueof_farenheit = float(input("Enter the value for the farenheit temperature\n"))

caculation_of_values = (valueof_farenheit - 32) * 5/9

print("The value for the farenheit temperature is", caculation_of_values)
