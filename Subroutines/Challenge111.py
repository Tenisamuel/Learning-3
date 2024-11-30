#Program name: Level 7 Challenge 111 Timer incomplete
#Program asks user to set a timer for a number of seconds between 1 and 5

import time
waitTime = int(input("How many seconds (between 1 and 5) \
do you want to set the timer for? "))

#validate the user entry
#If not between 1 and 5, print message and ask user to re-enter

chooseAgain = True
while chooseAgain:
    if not (waitTime in (1,2,3,4,5)):
        waitTime = int(input("The value you inserted was wrong, please enter a between 1 to 5\n"))
    else:
        chooseAgain = False
        timer = waitTime

print("Start the timer...")
for second in range(1,timer + 1,1):
    print(second, "second")
    time.sleep(1)
            
#wait the required number of seconds before printing
print("Time's up!")



import time
waitTime = float(input("How many seconds (between 1 and 5) \
do you want to set the timer for? "))

while not(waitTime in range(1,6)):
    waitTime = float(input("Enter a number between 1 and 5! "))    

print("Start the timer...")
time.sleep(waitTime)
print("Time's up!")