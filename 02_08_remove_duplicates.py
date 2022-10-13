# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
new_list = [ ]

for i in list_:
    occurence = list_.count(i)
    #print(i)
    #print(occurence)
    if occurence == 1:
        #print(i)
        new_list.append(i)
           
    elif occurence > 1:
        continue

print(new_list)