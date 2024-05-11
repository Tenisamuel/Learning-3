#Write a program to ask the user to enter the number of lengths swum by jane on a certain day if the number of
#lengths is not between 10 and 150,ask the user to re enter until a valid length is entered.print a short
#message "Data accepted" when valid data is entered.

length = int(input("Enter the Length that is assumed to be swum by Jane: \n"))

while length not in range(10,151):
    print("You enter the wrong value, You need to satisfy the condition of the length swum by Jane\n\n")
    length = int(input("Re-Enter the length swum by Jane\n"))

print("Data Accepted")