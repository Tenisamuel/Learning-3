# This is the program that converts the age of a dog to that of a human using some following methods.

age_of_dog = int(input("Enter the age of the dog: \n"))

if age_of_dog <= 2:
    human_age = 12 * age_of_dog
    print ("The human age for this is", human_age)
elif age_of_dog > 2:
    human_age = 24 + ((age_of_dog - 2) * 6)
    print ("The human age is given to be as ", human_age)
