# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

input_dict = {"item1": 5, "item2": 6, "item3": 1}
empty_list = []

for key, value in input_dict.items():
    items = key, value
    the_tuples = tuple(items)
    empty_list.append(the_tuples)
    #for value in input_dict.items():
    #    print(items)
    empty_list.sort()
print(empty_list)








