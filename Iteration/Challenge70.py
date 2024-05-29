#Write a program to:
    #Allow the user to enter the names and years of five olympic games cites.
    #Calculate and print the names and years of the two cites with the most recent and earliest years

max_year = 0
min_year = 10**8 
max_city = ""
min_city = ""

for i in range(5):
    city = str(input("Enter 5 cities in the olympic games"))
    year = int(input("Enter the 5 years of the cities you have picked in the olympic cites"))
    if year > max_year:
        max_city = city
        max_year = year
    if year < min_year:
        min_city = city
        min_year = year
        

