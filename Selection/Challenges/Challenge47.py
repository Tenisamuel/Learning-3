#Write a program to measure a user's resting heart rate.

#Ask the user. "Have you been at rest for at least 20 minutes?"

#if the user inputs "Y" , ask the user "is your pulse rate between 60 and 100 bpm?"

#if their pulse rate is between 60 and 100 bpm, print "Your heart rate is within the expected range"
#otherwise print "Your resting heart rate is outside of the expected range. you may wish to seek 
#attention from a proffesional.

#" if the user inputs "N", print "Rest for 20 minutes and try again" 

time_rested = input("Have you been at rest for at least 20 minutes?\n")
if time_rested == "Y" or time_rested == "y":
    heartrate =  int(input("is your pulse rate between 60 and 100 bpm\n"))
    if (heartrate > 60) and (heartrate < 100):
        print("Your heart rate is within the expected range\n")
    else:
        print("Your resting heart rate is outside of the expected range\n")
else:
    print("Rest for 20 minutes and try again")
    