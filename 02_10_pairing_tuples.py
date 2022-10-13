# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
the_randlist = randlist
empty_tuple = ()


for i in the_randlist:
    the_randlist.sort()
    #the_slice = the_randlist[0:2]
    #tuplit = tuple(the_slice)
    
#print(tuplit)

def grouper(n):
    for n in the_randlist:
        tuplit = tuple(n)
        len(tuplit) == 2
        return tuplit

print(grouper(the_randlist))

#go through the list 
#sort the list in ascending order 
#take each item and put it into a tuple 
#if the tuple has two items, close it and open another tuple 
#do this until all items from the list are in a tuple 