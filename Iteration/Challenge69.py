




totaltime = 0
mintime=10
moredata = True
while moredata:
    nameofdiver = input("Enter name of diver\n")
    if nameofdiver != "xxx":
        scoreofdiver = float(input("Enter your score out of 10 "+ nameofdiver + ": "))
        if scoreofdiver >=1 and  scoreofdiver <=10:
            moredata =  True
            if scoreofdiver < mintime:
                mintime = scoreofdiver
                fastestdiver = nameofdiver
    else:
        moredata = False
print("Fastest diver:",fastestdiver)
print("Time:", round (mintime,1), "seconds")