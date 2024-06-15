#Write a program to ask the user to enter the number of 12 astronauts sent on space missions
#in the years 2016 to 2020 e.g "How many astronauts on space missions in 2016?" 

#store the number in a list named astronauts

#Print the list list and the total number of astronauts sent on space missions from 2016 to 2020

astronauts = []

for i in range(0,12):
    prompt = input("Write down a list of astronauts that were in space in 2016\n")
    astronauts.append(prompt)

print("The following were the names of astronauts that were on space missions in 2016:", astronauts)
print("There were", len(astronauts), "elements")