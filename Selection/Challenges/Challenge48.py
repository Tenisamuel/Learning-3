#Program name: Level 3 Challenge 48 Challenge Fast cash incomplete
#program simulates selecting "Fast cash" at ATM

print("1. Balance enquiry")
print("2. Mini statement")
print("3. Fast cash\n")

#The escape sequence \n causes an extra new, blank line

print("Please select a transaction")

choice = input("Click either 1, 2 or 3")

if choice == "1":
    print("Option 1 selected: balance printed")

elif choice == "2":
    print("option 2 selected:mini statement printed")

elif choice == "3":
    print("Option 3 selected: Fast cash" )
    amount = input("select amount in £: 20, 50 or 100: ")
    if not ((amount == "20") or (amount == "50") or (amount == "100")):
        print("Invalid amount")

    else:
        print("£" + amount + " dispensed")
        print("Please take your cash")

else:
    print("Invalid selection")