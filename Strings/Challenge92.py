#Complete the program to assign the following text to a string variable notice: "All Coast bound trains
# will now depart from platform 4. Passengers should wait on platform 4."
#Use a string method to replace both occurrences of "4" with "2a" and print the resulting sentence.


#Program name:Challenge 92 String replcement
#This program replaces all occurrences of "Platform 4" with "Platform 2A" in a string

notice = "All coast bound trains will now depaart from platform 4.\n\"passengers should wait on Platform 4"

newnotice ="All coast bound trains will now depaart from Platform 4.\n\"passengers should wait on Platform 4"

replacement = newnotice.replace("Platform 4", "Platform 2a")

print(replacement)