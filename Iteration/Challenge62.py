#Write a program to ask the user to enter the number of lengths swum by jane on a certain day if the number of
#lengths is not between 10 and 150,ask the user to re enter until a valid length is entered.print a short
#message "Data accepted" when valid data is entered.

lengths = int(input("Write a number asumed to be the length of jane if she swam between the lengths 10 and 150\n"))

while lengths not in range (10,151):
    print("Re-enter a value between 10 and 150 you must satisfy the condition")
    lengths = int(input("Write a number asumed to be the length if jane between 10 and 150\n"))

print("Good answer")