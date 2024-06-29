#Create two lists.One list contains the names of eight plantes.The second list Contains the sizes of the planets
#in percentages relative them.
#Jupiter 1120% the size of Earth.
#Saturn 945% the the size of Earth.
#Uranus 400% the size of Earth.
#Neptune 390% the size of Earth.
#Venus 95% the size of Earth.
#Mars 53% the size of Earth.
#Mecury 38% the size of Earth.
#Earth 100% the size of Earth.

#From the two lists, print the information in the format given above.

nameofplanets = ["Jupiter","Saturn","Uranus","Neptune","Venus","Mars","Mecury","Earth"]

sizesoflist = [1120,945,400,390,95,53,38,100]

for i in range(len(nameofplanets)):
    print(nameofplanets[i], str(sizesoflist[i])+"% of the size of the earth")