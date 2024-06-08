#Write a program to initialise and print the list of planets:
#planet = ["Mecury", "Venus,", "Earth", "Mars", "Jupiter", "Saturn"]

#Then print the list with each planet on a seperate line starting with saturn, and ending with mecury.

planets_on_next_line = ["Mecury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]

print(*planets_on_next_line, sep="\n")