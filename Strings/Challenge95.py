#Write a program which asks a user to enter a new password. The password must be at least 10 characters long
#and the user is repeatedly asked to re-enter password if it is less than 10 characters.

#Once the user has entered a valid password, the user is asked to verify it by entering it a second time.If it matches, 
#the message "Password accepted" is pribted and the program terminates.

print("Your password must be at least 10 characters long")

validPassword = False

while not validPassword:
    validPassword = True
    password1 = input("Please enter password: ")
    if len(password1) < 10:
        validPassword = False
        print("Must be at least 10 characters")

password2 = input("Please enter password a second time: ")   
if password2 == password1:    
    print("Password accepted")
else:
    print("passwords don't match")
       

