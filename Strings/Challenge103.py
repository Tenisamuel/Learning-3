#Program name: Level 6 Challenge 103 Strawberries incomplete
#Program gives information about strawberry varieties

print("The list below shows the types of strawberry plants in stock.")

#display options:

print("        Variety")
print("{:^8d}{:<15}".format(1, "Christine"))
print("{:^8d}{:<15}".format(2, "Vibrant"))
print("{:^8d}{:<15}".format(3, "Honeoye"))
print("{:^8d}{:<15}".format(4, "Cambridge"))
print("{:^8d{:<15}}".format(5, "Pegasus"))
      
#input selected variety. (Must be between 1 and 5, or 0 to end)

chooseAgain = False
while chooseAgain == True:
    variety = input("Select variety (1-5) to view description (0 to end): ")
    if  not(variety in (.......................)):
        print ("Invalid choice")
    elif variety == "0":
        ..........................    
    else:          
        if variety ==1 or variety == 2:
            print("Christine and Vibrant - Ready to pick early June")
            print("Large, sweet and delicious")
        elif variety == 3:
            print("Honeoye - Ready to pick from mid-June")
            print("Good for jam-making")
        elif variety == 4 or ..................
            print("Cambridge and Pegasus - Juicy and soft")
            print("Pick late June to late July")
        
print("Thank you - more choices available soon!")