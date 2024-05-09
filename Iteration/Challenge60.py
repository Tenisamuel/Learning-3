#Write a program to display the times tables 7 to 10, displaying each table in format 7 x 1 = 7 etc.

Timestable_two = int(input("Write the following timestables you want to b displayed 7,8,9 or 10\n"))

if (Timestable_two >= 7) and (Timestable_two <= 10):
    for i in range(1,13):
        result = Timestable_two * i
        print(Timestable_two, "X", i, " =", result)

else:
    print("You have to satisfy the condition above")

