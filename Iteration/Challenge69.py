#Enter the names and scores out of 10 (e.g 7.5) achieved by divers in a competion.The end data is indicated
#by a name of xxx.print the names and scores of the diver with the best scores,rounded to 1 decimal place. (Assume
#there are no ties for the first place)

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