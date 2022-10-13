# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

from itertools import count


my_list = [2, 4, 6, 8, 2, 8, "me", "you"]
new_list = []

for i in my_list:
    #print(i)
    occurence = my_list.count(i)
    if occurence == 1:
        new_list.append(i)
        print(new_list)


