# Create a list of random numbers and inside the list, count any of the number that has 1 as one entity.
# For example a list of 21,8,56,378,301,88,17,13,61
# The number of "1" that occurs is 5

#random_numbers = ["56","20","43","52","99","50","64","22","18","61","89","77"]

#count = 0

#for i in random_numbers:
#        if "1" in i:
#            count = count + 1


#print("The amount of numbers that have 1 in it are", count)

#import turtle
#window = turtle.screen


#def sum(a, b):
#    total = a + b
#    return total




#two_numbers = int(input("Enter a number"))
#list = []

#for i in range(two_numbers):
#    list1 = list.append(int(input()))

#sum_list1 = 0
#for i in list:
#    sum_list1 = sum_list1 + i



#print("Calculated numbers are", sum_list1)
#first_number = int(input("Enter a number: "))
#second_number = int(input("Enter second number: "))

#calculation = first_number + second_number

#print("This is your two numbers summed together", calculation)


print("This program will either help you multiply,subtract or add")

m_s_a = input("Would you like to multiply,subtract or add\n")

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if m_s_a == "multiply":
    num = number1 * number2
    print(num)
elif m_s_a == "subtract":
    num2 = number1 - number2
    print(num2)
elif m_s_a == "add":
    num3 = number1 + number2
    print(num3)
else:
    print("please satisfy the condition")

    import string
#Modules have been imported to print unpredictable values
#string module gives a premade set of characters that 
#saves time printing everysingle alphabet, letter, character etc.
def generate_password():
    #Function used to hold all necessary prompts for the user to enter 
    #what sort of password they may want depending on their preference
    #Functions such as .strip() and .lower() remove spaces in between when the prompts are called
    #.lower() coverts every input into lowercase
    while True:
        # as the input is still true keep running the program unitl it breaks,
        #The break signifies the correct input has been entered.
        try:
            length = int(input("Enter the desired password length: ").strip())
            break
        except ValueError:
            print("Invalid input, please enter a number.")

    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    #Other necessary prompts to allow the user construct their password with ease.

    if length < 4:
        print("Password length must be at least 4 characters.")
        return ""
    #This check validates the inputs from the user and IF the length of the password
    #Is below 4, it isnt strong enough and is more likely to guess or hack the password.
    lowercase_letters = string.ascii_lowercase if include_lowercase == "yes" else ""
    uppercase_letters = string.ascii_uppercase if include_uppercase == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    special_characters = string.punctuation if include_special == "yes" else ""
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if not all_characters:
        print("No character types selected. Aborting.")
        return ""

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase_letters))
    if include_lowercase == "yes":
        required_characters.append(random.choice(lowercase_letters))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))
    if include_special == "yes":
        required_characters.append(random.choice(special_characters))

    remaining_length = length - len(required_characters)
    password = list(required_characters)

    for _ in range(remaining_length):
        characters = random.choice(all_characters)
        password.append(characters)
    random.shuffle(password)  # Shuffled to make password stronger
    str_password = "".join(password)
    return str_password
password = generate_password()
print(password)
print("------------------------------------------")