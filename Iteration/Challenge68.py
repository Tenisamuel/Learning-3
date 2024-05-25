#Amend the program Challenge 68 Double a number repeatedly completed so that the user canenter the final target.
#include validation to ensure the target entered by the user is between 20 and 100,000. Also include a print 
#statement so that the number, and number of time is doubled,is printed each time.

#validate the user entry of initial starting number
validNum = False
while not validNum:
    num = int(input("Enter a number between 1 and 10: "))
    if num >= 1 and num <= 10:
        validNum = True
    else:
        validNum = False
        print("\nInvalid number!")


#validate the user entry of final target
validTarget = False
while not validTarget:
    target = int(input("Enter a final target between 20 and 100000: "))
    if target >= 20 and target <= 100000:
        validTarget = True
    else:
        validTarget = False
        print("\nInvalid number!")

#initialise count

count = 0


#double the input number until num >= 100000
while num < target:
    num = num * 2
    count = count + 1
    print(count, num)

#print the result and how many times the number was doubled
print("Final number:",num, " Number of times doubled:",count)