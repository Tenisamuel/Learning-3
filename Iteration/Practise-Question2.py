#write a program to ask the user to input two positive integers x and y where y > x. print all the numbers
#between x and y inclusive that are divisible by 9. Also write a test to make sure that this condition
#is satisfied

first_positive_integer_y = int(input("Write the first positive integer\n"))

second_positive_integer_x = int(input("Write the second positive integer\n"))

if (first_positive_integer_y > second_positive_integer_x):
    for i in range(first_positive_integer_y,second_positive_integer_x+1):
        if(i % 9 ==0):
            print(i)



else:
    print("The value of y is greater than x, you need to satisfy the condition")