#A car rental firm asks a customer to answer "Y" or "N" to the question "Are you aged 25 or over?".Write a boolean 
#Expression using the string method upper() to check if the user response assigned to variable response is either
#"y" or "Y".



print("Are you aged 25 or over?")
answer = input("enter Y or N to the question above")
entered_answer = answer.upper()
if entered_answer == "Y":
    print("Okay")
elif entered_answer == "N":
    print("Oh, okay")
else:
    print("So, your younger ")