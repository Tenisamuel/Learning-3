#Program name: Level 7 Challenge 111 Timer incomplete
#Program asks user to set a timer for a number of seconds between 1 and 5

import time
waitTime = int(input("How many seconds (between 1 and 5) \
do you want to set the timer for? "))

#validate the user entry
#If not between 1 and 5, print message and ask user to re-enter

if not (waitTime in (1,2,3,4,5)):
    print("Re-enter")
    

print("Start the timer...")
............................

#wait the required number of seconds before printing
print("Time's up!")