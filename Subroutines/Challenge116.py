#Write a program which asks  the user to enter in the format hhmmss the number of hours, minutes and seconds
#taken by a runner to complete a marathon. Call a subroutine to convert the number of seconds. In the main 
#program, print the number of seconds taken. (TIP: use string slicing)

#Test your program by entering a time of 2 hours, 1 minute and 1 second in the format 020101. The expected result
#IS 7261 SECONDS.

#What happens if you enter 211 instead of 020101.

#It gives you an error

hours_min_seconds = input("Enter the time of the runner in format hhmmss")

slice1 = hours_min_seconds[0:2]
slice2 = hours_min_seconds[2:4] 
slice3 = hours_min_seconds[4:6] 

int_slice1 = int(slice1) * 3600
int_slice2 = int(slice2) * 60
int_slice3 = int(slice3)

print (int_slice1+int_slice2+int_slice3)
