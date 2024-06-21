#Program name: Level 5 Challenge 77 Lists planet and moons with errors

planetList = []
moonList = []
moreData = True
print("\nPlanets and moons\n")

while moreData:
    planetName = input("Enter name of planet, xxx to finish: ")
    if planetName == "xxx":
        moreData = False
    else:
        numMoons = int(input("Enter number of moons: "))
        planetList.append(planetName)
        moonList.append(numMoons)

for index in range(len(planetList)):
    print(planetList[index] + " has " + str(moonList[index]) + " moons")