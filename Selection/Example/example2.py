# Write a simple program that prepares the food menu of a family member has been produced. The name of the family member are given as
#Teni, Michael, Richard, Pelumi, Desmond, Usman, Nasiru. The program prepares the food menu using the table given below.
# Teni -> (Rice and Beans)
# Michael -> (Egg and Yam)
# Richard -> (Ogbono and Pounded Yam)
# Pelumi -> (Beans and Bread)
# Desmond -> (Egusi and Fish and Eba)
# Usman -> (Beans and Yam)
# Nasiru -> (Potatoes and Eggs)
# Other people that is not part of the family will be asked to leave the program 

Family_Member = input("Hello,Who are you, Can you tell me your name?\n")

if Family_Member == "Teni":
    print("Hello Teni, I have been instructed to serve you rice and beans")

elif Family_Member == "Micheal":
    print("Hello Micheal, I have been instructed to make you Egg and yam")

elif Family_Member == "Richard":
    print("Hi Richard, I have been asked to prepare you ogbono and pounded yam")

elif Family_Member == "Pelumi":
    print("Hello Pelumi, I have Beans and bread for you to eat")

elif Family_Member == "Desmond":
    print("Hello Desmond, I have been instructed to give you Egusi, Fish and Eba")

elif Family_Member == "Usman":
    print("Hi Usman,  I have been asked to make you Beans and Yam")

elif Family_Member == "Nasiru":
    print("Hello Nasiru,I have been asked to serve you potatoes and eggs")

else:
    print("You are not part of this family please leave this program")
