#Write a program which prints the names of the largest and the smallest planets in the lists described.
#Program name: Challenge 81 largest and smallest planets
planet = ["Jupiter","Saturn","Uranus",\
          "Neptune","Venus","Mars", "Mercury","Earth"]
size = [1120,945,400,390,95,53,38,100]


#initialise variables
numberOfPlanets = len(planet)

#initialise max and min values to size of first item in each list
minSize = size[0]
minPlanet = planet[0]
maxSize = size[0]
maxPlanet= planet[0]

#check size of each planet except the first planet
for n in range(1,numberOfPlanets):
    if size[n] > maxSize:
        maxSize = size[n]
        maxPlanet = planet[n]
    if size[n] < minSize:
        minSize = size[n]
        minPlanet = planet[n]

print("Largest planet: "+str(maxPlanet)+"'s radius "+str(maxSize)+"% of earth's radius")
print("Smallest planet: "+str(minPlanet)+"'s radius "+str(minSize)+"% of earth's radius")


