#Complete the program below to check tyre pressure. if it is between 28 psi and 32 psi, print "Tyre pressure OK"
#Otherwise, print "Tyre pressure is too high or too low"

#This is the variable of the pressure
pressure = int(input("Type tyre pressure in psi: "))

#This python statement is used to caculate the pressure of the tyre between 28 and 32.
#If the pressure is in between 28 and 32 it is ok, if it is higher than 32 it is too high 
#but if lower than 28 is too low. 

if (pressure < 28):
    print("Tyre pressure is too low")

elif (pressure > 32):
    print("Pressure is too high")

else:
    print("Tyre pressure is OK")

