#Program name: Level 3 Challenge 49 Siren decibels test incomplete
#The program determines whether a recorded level of decibels meets the
#acceptable minimum requirement for each of three models produced in a factory.

#Specify the minimum accepted decibels 
#on different sirens for quality control tests.
print("Minimum decibels accepted per model:")
print("Model A (A): 93 dB")
print("Model B (B): 110 dB")
print("Model C (C): 110 dB")
print("Model D (D): 126 dB")
print("Model E (E): 154 dB")
print("Model F (F): 186 dB")

#ask user to input model and recorded decibel test reading
print("Which model has been tested? ")
model = input("Enter A for Model A, B for Model B or C for Model C:\n")
    
reading = float(input("What is the recorded decibel level\n"))  

#test that decibel level is above minimum tolerances
if reading < 93:
    print("The siren has failed the minimum acceptable limit for all models.")    

elif model == "a" or model == "A":    
    print("Passed.") 

elif model == "b" or model == "B":
    if reading < 110:
        print("Failed. Requires adjustment or reclassification as Model A.")
    else:
        print("Passed.")

elif model == "c" or model == "C":
    if reading < 110:
        print("Failed. Requires adjustment or reclassification.")
    else:
        print("Passed.")

elif model == "d" or model == "D":
    if reading < 126:
        print("Failed. Requires adjustment or reclassification.")
    else:
        print("passed")

elif model == "e" or model =="E":
    if reading < 154:
        print("Failed. Requires adjustment or reclassification.")
    else:
        print("Passed")

elif model == "f" or model == "F":
    if reading < 186:
        print("Failed. Requires adjustment or reclassification.")
    else:
        print("passed")

else:
    #invalid model entered
    print("Model must be A, B or C. No result given.")