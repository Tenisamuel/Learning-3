#Write a program to count numbers from 0 to 100 in 5s snd print them on one line.

backwards = [i for i in range (0,105,5)]
print(backwards)

#  OR

for i in range (0,105,5):
    print(i, end = " ") 