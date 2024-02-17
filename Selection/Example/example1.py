#The program inputs the current battery charge on a mobile phone. if it is below 10%, it prints "Low battery,
#Please Charge.". if it is between 25% and 99% it prints "Good Charged Battery.". if it is above 150% "Fully Done.".

battery_input = int(input("Enter the percentage of the Battery: \n"))

if battery_input < 10:
    print("Low battery")

elif battery_input > 150:
   print("Fully Charged")

else:
  print("Good Charged battery")
    