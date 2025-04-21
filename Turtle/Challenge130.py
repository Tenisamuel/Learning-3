master_pwd = input("What is the master password").lower()

def view():
    pass

def add():
    pass



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