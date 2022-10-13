# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

#print(randlist)

get_numbers = tuple(input("give a list of number:"))
print(get_numbers)

for n in get_numbers:
    #print(n)
    if n >= n in get_numbers:
        print(f"this is the highest number:{n}")

