#write a program which:
    #asks a user to enter their firstname, surname, and date of birth in the format ddmmyy
    #calls a subroutine which creates username consisting of the first two letters of surname
    #followed by first two letters of firstname (both in uppercase) and date of birth.For example,
    #Thomas vincent born 18/01/2005 will be given username VITH180105
    #TIP: USE STRING SLICING, concatenation and method string.upper().see page 44
    #return the username to the main program and prints it.

firstname = input("Enter your firstname")
surname = input("Enter your surname")
dob = input("Enter yor date of birth in the format ddmmyy")

slice = firstname[0:2].upper()
slice_two = surname[0:2].upper()

print(slice + slice_two + dob)