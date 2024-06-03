#Write a program to initialise the list:
#["Mercury, "Venus", "Mars", "Jupiter", "Saturn"]
#Use a list method to insert "Earth" between "Venus" and "Mars" print the ammended list

planet_five = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
planet_five.append("Earth")

planet_five[2] = "Earth"

print(planet_five)