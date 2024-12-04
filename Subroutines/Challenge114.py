#Write a program which asks the user to input their firstname and then calls a procedure which prints
#"Hello jane" or whatevername entered
def firstname():
    print("Enter your first name")
    firstname = input("Enter your name")
    print("Hello", firstname)
    return firstname
option = firstname()