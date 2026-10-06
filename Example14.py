MyText = input("Enter a string:")

if MyText.isdigit():
    print("You entered digits only")
elif MyText.isalpha():
    print("You entered alphabets only")
elif MyText.isalnum():
    print("You entered a mix of numbers and alphabets")
else:
    print("You entered other characters")