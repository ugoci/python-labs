# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

from dataclasses import replace


convertible = True
string = "codingnomads"

while convertible:
    tuplit = tuple(string)
    print(tuplit)
    listit = tuplit.split()
    print(listit)
    for i in listit:
        replacer = replace("c","k") 
        print(listit)
        convertible = False