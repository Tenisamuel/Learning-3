#Write a python program to intitialise and print the lists described in challenge 78 and to amend the value for neptune
#in th list given in challenge 78. it should be 388%. Print the original lists and print the amended value, e.g
#Neptune 388%

nameofplanets = ["Jupiter","Saturn","Uranus","Neptune","Venus","Mars","Mecury","Earth"]

sizesoflist = [1120,945,400,390,95,53,38,100]

for i in range(len(nameofplanets)):
    sizesoflist[3] = 388
    print(nameofplanets[i], str(sizesoflist[i])+"% of the size of the earth")