#Write a program to ask the user to enter the area of ocean (in square nautical miles) scheduled for cleanup each
#day to clear it for plastic pollution.One vessel can cover 12 square nautical miles per day. Calculate the smallest
#whole number of vessels rewired to operate the cleanup.

import math
areaprompt = int(input("Enter the area of the ocean (in square meters):"))
calculations = 12 * 12
print(math.floor(calculations))