#Write a program which asks a user to enter a new password. The password must be at least 10 characters long
#and the user is repeatedly asked to re-enter password if it is less than 10 characters.

#Once the user has entered a valid password, the user is asked to verify it by entering it a second time.If it matches, 
#the message "Password accepted" is pribted and the program terminates.

Promptpassword = input("Enter your password: ")
while len(Promptpassword) < 10:
    print("Re-enter password")
    if len(Promptpassword) > 10:
         Promptpassword = (input("Enter the password again to verify your password"))
         if Promptpassword == Promptpassword:
            print("Password match")
       

