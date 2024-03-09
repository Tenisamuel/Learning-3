#Write a program to measure a user's resting heart rate. Ask the user, "Have you been at rest for at least"
#"20 minutes" if the user inputs "Y" , ask the user "is your pulse rate between 60 and 100bpm?"

#If their pulse is between 60 and 100 bpm, print "your heart rate is within the expected range" otherwise print
#"your resting heart rate is outside of the expected range. you may wish to see a proffesional"

#If the user priints "N". print "Rest for 20 minutes and try again !"

first_question = str(input("Have you been at rest for at least 20 minutes"))

if first_question == "Y":
    second_question = str(input("Is your heart rate between 60 and 100bpm?"))

    if second_question == "Y":
        print("Your heart rate is within the expected range ")

    else:
        print("your resting heart rate is outside of the expected range. you may wish to see a proffesional")
elif first_question == "N":
    print("Rest for 20 minutes and try again !")