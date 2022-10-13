# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_3 = {}
#t = dict_1 | dict_2 # what does this mean? It combined both dictionaries in a weird way
#new_dict = dict_1 dict_2

#add all keys to the new dictionary 
#add all values to the new dictionary 
#if a key appears in both dictionaries, add the values for both dictionaries 

for key, value, in dict_1.items():
    dict_3[key] = value

    for key, value, in dict_2.items():
        dict_3[key] = value 

print(dict_3)



