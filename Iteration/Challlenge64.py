#Enter,save and run the program in Example 8. What does the promt say now?

day = 0
totallengths = 0
moredata =  True
print("Enter -1 when no more data")
while moredata:
    lengths = int(input("Enter number of lengths on day" + str(day+1)+ ": "))
    if lengths != -1:
        day = day+1
        totallengths = totallengths + lengths
    else:
        moredata = False
averagelengths = totallengths / day
print("Average daily number of lengths:", round(averagelengths, 1))
