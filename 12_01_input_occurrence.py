# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4



from ast import Break


for i in range(1):
    first = input("say a word:  ")
    second = input("say a letter:  ")
    trouve = first.index(second)
    
    if second in first:
        print("Result:", trouve)

    elif second not in first:
        print("The letter is not in the word")
    
    else:
        print("end")
