#Keybinds = input("Enter your edit bind")
#Prompt takes the information from the user about their edit bind
#if Keybinds == "F":
    #Use of selection to categorise the choices therefore if the 
    #selected option F is chosen it would display comp otherwise the following...
#    print("Comp")
#else:

#    print("Thats aight i guess")
#area = input("Are you looking for the area of a circle yes or no")
#radius = float(input("Enter the radius of your circle"))
#if area == "y" or area ==  "Y":
#    calc = 3.141592 * radius**2
#    print(calc)
#else:
#    final_calc = 3.141592 * 2 * radius
#    print(final_calc)

Number_one = int(input("Enter the first number"))
Number_twon = int(input("Enter a second number"))
if isinstance(Number_one, int) and isinstance(Number_twon, int):
    print(Number_one+Number_twon)
    print(Number_one - Number_twon)
    print(Number_one * Number_twon)
    print(Number_one / Number_twon)