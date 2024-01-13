#Complete the program challenge 17 Divide books among children incomplete in the python programs/Starred 
#Challenges(incomplete)
#folder The program is designed to specify the total nu,ber of books available to be given to a group of 
#children. it then caculates
#And prints how many books each child will receive and how many will be left over.
books = 700
children = 190
Resultperchild = books//children
print("This is the amount of books for each child", Resultperchild)
Resultofbooksleftover = books%children
print("This is the amount of books remaining", Resultofbooksleftover)