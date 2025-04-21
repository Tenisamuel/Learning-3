master_pwd = input("What is the master password").lower()

def view():

    with open("Passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:", user, ", Password:",passw)
        

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("Passwords.txt", 'a') as f:
        f.write(name + "|"+ pwd +"\n")


while True:
    mode = input("Would you like to add in a new password or  view exsisting ones (view, add)?").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue