#The program inputs the current battery charge on a mobile phone. if it is below 15%, it prints "The battery.
#needs to be charged required.". if it is between 16% and 80% it prints "Optimal Battery, Good Condition.". if it is above 80% "Fully Charged.".

battery_input = int(input("Enter the percentage of the Battery: \n"))

if battery_input < 20:
    print("Low Battery, Charge required")
elif battery_input == 100:
    print("Fully Charged")
else:
    print("Battery charge OK")