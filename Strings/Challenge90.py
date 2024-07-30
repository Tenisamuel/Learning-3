#Write a program to ask the user to  enter a sentence. Calculate and print the number of times the letter 
#"e" appears in the sentence.


sentence = input("Enter the sentence:")

count = 0

for i in sentence:
    if i == "e":
        count = count + 1

print("The number of 'e' in the sentence is given as:", count)