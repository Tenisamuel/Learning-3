#Write a test plan for challenge 55 to include test data for different user entries, 
#together when expected results. Test your program

type_first_positive_integer_a = int(input("Write the first positive integer:\n"))

type_second_positive_integer_b= int(input("Write the second positive integer:\n"))

print("\n")

if (type_first_positive_integer_a < type_second_positive_integer_b):
    for i in range(type_first_positive_integer_a,type_second_positive_integer_b + 1):
        print(type_first_positive_integer_a, type_second_positive_integer_b)

else:
    print("The value of a is greater than b, you need to satisfy the condition")