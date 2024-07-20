#Program name: Level 5 Challenge 85 Figure skating competition incomplete
#Five skaters are awarded scores by 3 different judges

#initialise lists
score = [ [75, 59, 63],  
          [88, 91, 94],  
          [78, 81, 84],
          [65, 69, 73],
          [90, 84, 69]]

#initialise list of skaters' names
#names are Amber, Cindy, Valentina, Isabella, Terri
name = ["Amber", "Cindy", "Valentina", "Isabella", "Terri"]

#initialise list of five totals
#total = [sum(score[0]), sum(score[1]), sum(score[2]), sum(score[3]), sum(score[4]) ]

total = [0]*5

#initialise maxScore
maxScore = 0

for skater in range(5):
    for judge in range(3):
        total[skater] = total[skater] + score[skater][judge]
    if total[skater] > maxScore:
        maxScore = total[skater]
        winnerName = name[skater]

print("Winner:", winnerName, " Score:", maxScore)






