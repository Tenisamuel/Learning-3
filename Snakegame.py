import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value )

    return roll
while True: 
    players = input("Enter a value between 1 - 4")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores < max_score):
    should_roll = input("Do you want to roll? (y)")
    if should_roll.lower() == "y":
        break
    
    value = roll()