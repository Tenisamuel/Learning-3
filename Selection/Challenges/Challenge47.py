#Write a program to measure a user's resting heart rate. Ask the user, "Have you been at rest for at least"
#"20 minutes" if the user inputs "Y" , ask the user "is your pulse rate between 60 and 100bpm?"

#If their pulse is between 60 and 100 bpm, print "your heart rate is within the expected range" otherwise print
#"your resting heart rate is outside of the expected range. you may wish to see a proffesional,"

#If the user priints "N". print "Rest for 20 minutes and try again !"

rest_time = str(input ("Have you been at rest for at least 20 minutes?"))
heartrate = str(input("is your pulse rate between 60 and 100bpm?"))

if rest_time == "Y":

elif heartrate  > 60:
    print("Your heart rate is at the expected range") 

elif heartrate < 100:
    print("Your heart rate is at the expected range") 

