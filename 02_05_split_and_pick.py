# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user_input = input("what's up?:")

for i in user_input:
    list_maker = user_input.split()
    
    for e in list_maker:
        occurence = list_maker.count(e)
        
        if occurence > 1:
            print(e, ":occurs", occurence)
        
        elif occurence == 1:
            print(e, ":occurs once")
    break

    