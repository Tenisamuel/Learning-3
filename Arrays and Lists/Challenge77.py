planetlist = []
moonList = []
moreData = True
print("\nPlanets and moons\n")

while moreData:
    planetName = input("Enter name of planet, xxx to finish: ")
    if planetName == "xxx":
        moreData = False
    else:
        numMoons = int(input("Enter number of moons: "))
        planetlist.append(planetlist)
        moonList.append(numMoons)

for index in range(len(planetlist)):
    print(planetlist[index], "has" , (moonList[index]) , " moons")