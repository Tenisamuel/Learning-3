#The program asks the user to enter a number between 1 and 10. if the number is not in thi range, keep printing
#a warning message and asking the user to re enter the number. Then keep doubling this number until the result
# 100,000 or more.=print the final result and the number of times the number was doubled.

validNum = False
while not validNum:
    num = int(input("Enter a number between 1 and 10: "))
    if num >= 1 and num <= 10:
        validNum = True
        print("The number will be doubled repeatedly until the result >= 100,000")
    else:
        validNum = False
        print ("\nInvalid number!")

#initialise count

count = 0


#double the input number until num >= 100,000
while num < 100000:
    num = num * 2
    count = count + 1

#print the result and how many times the number was doubled
print("Final number:",num, " Number of times doubled:",count)