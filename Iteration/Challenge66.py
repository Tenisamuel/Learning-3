#The program asks the user to enter the size in m square of an area that needs tiling. The user then selects
#The size of tiles they want from a range of sizes given in cm. The program tells them how many tiles 
#they would need (Ten percent is added to the caculated number to allow for tiles that need to be cut, and
#this number is rounded down to the nearest whole number)

#Copy and complete the program and save it in your own folder.

#Test your completed program by entering 20cm for tile length, 12cm for tile width and 2.4m square for area to
#covered.The integer number of tiles required, including the 10% extra, is 110. 

areaRequired = float(input("Enter area that requires tiling in sq m: "))

#validate the user's input for chosen length and width of tile
#Length must be 10, 15 or 20
#Width must be 9 or 12
#If value of either length or width is invalid, user is asked to re-enter

validLength = False
while not validLength:
    tileLength = input("Enter chosen length of tile in cm (10, 15 or 20): ")
    if tileLength in("10","15","20"):
        #convert input string to integer
        tileLength =int(tileLength)
        validLength = True
    else:
        print("Invalid length")             

#validate user input for width - must be 9 or 12

validWidth = False
while not validWidth:
    tileWidth = input("Enter chosen width of tile in cm (9 or 12): ")
    if tileWidth in("9","12"):
        tileWidth =int(tileWidth)
        validWidth = True
    else:
        print("Invalid length")  



numberOfTiles = (areaRequired * 100 * 100)/(tileLength * tileWidth)

print("Number of tiles to cover area:",int(numberOfTiles*1.1))