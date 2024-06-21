#Program name: Level 5 Challenge 79 Delete item from list of planets incomplete
#Finds and deletes "Earth" in list of planets

planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]

#print list of planets 
print("List of planets: ", ................)

#print blank line
print()

earthFound = False
index = 0

while index in range(len(planet)) and not earthFound:
    if planet[index] == "Earth":

# complete statements here       
        earthIndex =..................
        earthFound = ..................

        #delete "Earth"        
        ..................

    else:
        index = index + 1

print("Earth found at index " + str(index) + " in the list")

print("List after deleting Earth:", ..............)