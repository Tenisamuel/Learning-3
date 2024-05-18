#Write a program to enter the names and times in seconds of runners participating in 100m race heats.
#The program should prompt for their time e.g.
#       Enter time in seconds for king,    R;
#The end of data is signalled by entering xxx for the runners name.
#print the average time in seconds of all the runners.

names_of_runners = str(input("Enter your name?\n"))

timeofrunners = int(input("Write your time in seconds\n"))

times = 0
totaltimeofrunners = 0

while timeofrunners != -1:
    times = times+1
    totaltimeofrunners = totaltimeofrunners + timeofrunners
    timeofrunners = int(input("write your time in seconds, -1 to end: "))
    averagetimes = totaltimeofrunners / times
    print("The average time in seconds",averagetimes)

# Teni : 36.5 seconds
# Samuel : 38.2 seconds
# Emeka : 39 seconds
# Uche : 41.2 seconds