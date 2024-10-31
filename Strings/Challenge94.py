#Program name: Level 6 Challenge 94 Book title incomplete
#This program locates a book title in a string and prints it

book = "The book by Damian Barr is called 'You will be safe here'"

#find the length of the string named book

lengthofbook = len(book)

#find the first single quote mark
location_singlequote = book[34]


# now slice the string to isolate the title

title = book[34:58]
print(title)