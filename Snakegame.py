import random
RPS = ["Rock" , "Paper" ,"Scissors"]
for i in range(5):
    userinputchoice = str(input("Enter Rock, Paper Or Scissors")).lower
    Computerchoice = random.choices(RPS)
    print(userinputchoice)
    print(Computerchoice)