#A store sells a brand of italian bathroom tiles in different lengths and widths.Tiles come in length
#of 10, 15, 20cm and in widths of 10 and 12cm, or in lengths of 4, 6 an 8 inches and in widths of 4 and 5 inches.
#Customers can select which units to use.

#Write a program to ask the user to choose their preferred units of measurement and then calculate and print,
#for each length and each width, the area covered 1 tile

units = input("Enter the units of the area you want to calculate: Answer C or I \n")

if units == "C" or units == "c":
    print("Tiles Calculations will be done in cm\n")
    for length in range(10,21,5):
        for width in range(10,13,2):
            area = length * width
            print("Length", length,"cm \n Width", width, "cm \n Area", area, "cm\n\n")

elif units == "I" or units == "i":
    print("Tiles Calculations will be done in inches")
    for length in range(4,9,2):
        for width in range(4,6):
            area = length * width
            print("Length", length,"inches \n Width", width, "inches \n Area", area, "inches\n\n")

else:
    print("You did not enter the answer that is required for your program")
            
