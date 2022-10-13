# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


import re


for i in range(1):
    say = input("say something smart:  ")
    char = input("write a character here:  ")
    rep = say[0]
    if rep in say:
        print(rep, "will be replaced by", char, "in the original text reproduced below: ")
        print(say.replace(rep, char))
        
          
   
   