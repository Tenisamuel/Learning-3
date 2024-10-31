#Program name: Level 6 Challenge 93 Product numbers incomplete
#This program processes a list of product numbers for televisions,
#printing all those with third and fourth digits equal to 32"

productCode = ["SN44-SHD","PS32-POR","HT60-BFS","SN32-UHD","SG32-SMT","SN55-4KS"]
for index in range(0,6):
    size = productCode[index]
    if size[2:4] == "32":
        print("The printed elements that that print out the number 32 are: ", size)
#    else:
#        print("it seems like there are no groups with the number 32")
         


         
        

