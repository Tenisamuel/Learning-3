#Program name: Level 3 Challenge 46 Quiz incomplete
#This program asks three quiz questions, and scores the answers

#(Correct answers are: hummingbird, False, bullfrog)

#initialize score
score = 0
print("Answer each of the following three questions:")
answer = input("\nWhich is the only bird that can fly backwards? \n\
(a) Hummingbird, (b) Swift, (c) Flamingo? ")

#Each correct answer scores 1

#correct answer is a
if answer == "a" or answer == "A":
    print("Correct Answer, you have gotten one point")
    score = score+1
else:
    print("Wrong Answer")

answer = input("\nYou can get warts from touching a toad - \n\
True (T) or False (F)? ")

#correct answer is F
if answer == "f" or answer == "F":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")

#correct answer is a
answer = input("\nWhich animal never sleeps? \n\
(a) bullfrog  (b) whale  (c) butterfly  ")

if answer == "a" or answer == "A":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")

answer = input("What is the primary purpose of a firewall in network security? \
               \n A. Encrypting data \n B. Monitoring network traffic \n C. Controlling access to network resources \
               \n D. Detecting malware")

if answer == "b" or answer == "B":
    score = score + 1
    print("Correct Answer")
else:
    print("Wrong Answer")

print("\nYou scored", score, "out of 3")
if score == 3:
    print("Well done!")
elif score == 2:
    print("Pretty good!")
elif score == 1:
    print("More nature study required...")
elif score == 0:
    print("Oops!, you did poorly")