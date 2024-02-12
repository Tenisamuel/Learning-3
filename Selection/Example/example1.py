#The program inputs the current battery charge on a mobile phone. if it is below 20%, it prints "Low battery.
#Charge required.". if it is between 21% and 99% it prints "Battery charge OK.". if it is 100% "Fully Charged.".

battery_input = int(input("Enter the percentage of the Battery: \n"))

if battery_input < 20:
    print("Low Battery, Charge required")
elif battery_input == 100:
    print("Fully Charged")
else:
    print("Battery charge OK")