#Write statements to ask a truck driver to enter the weight of thier goods in pound(lb), convert
#the data to an integer and add 24,340 lbs to it to adjust for the weight on the truck. print out
#the combined(laden) weight e.g
#The laden weight of the truck  is .... lbs
#Convert the weight to kilos and output the result as an integer. There are 2.2 lbs to a kg.

teni = 34
joy = 59

print(joy + teni)

#int_joy = int(joy)
#int_teni = int(teni)

#print(int_joy + int_teni)


goodsWeight = input("Enter the Weight of Goods in Pounds: \n")

integer_of_goodWeight = int(goodsWeight)

answer = integer_of_goodWeight + 24350

print("The total answer in pounds is:\n", answer, "lbs")

#This section of the code will converts the lbs to kg

kg_answer = answer/2.2

print("The answer of the weight in kg is:\n", kg_answer, "kg")