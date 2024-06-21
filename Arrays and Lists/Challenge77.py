<<<<<<< HEAD
#Program name: Level 5 Challenge 77 Lists planet and moons with errors

planetList = []
=======
planetlist = []
>>>>>>> a70c2d8b10a5ba7cfc9c19577fa23505baa4cf7e
moonList = []
moreData = True
print("\nPlanets and moons\n")

while moreData:
    planetName = input("Enter name of planet, xxx to finish: ")
    if planetName == "xxx":
        moreData = False
    else:
        numMoons = int(input("Enter number of moons: "))
<<<<<<< HEAD
        planetList.append(planetName)
=======
        planetlist.append(planetlist)
>>>>>>> a70c2d8b10a5ba7cfc9c19577fa23505baa4cf7e
        moonList.append(numMoons)

for index in range(len(planetlist)):
    print(planetlist[index], "has" , (moonList[index]) , " moons")