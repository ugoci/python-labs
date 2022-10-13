# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
from itertools import count
import pathlib

file_location = pathlib.Path("C:/Users/Ugo/Documents/School/Studying/Software Development/Coding Nomads/Python 201/03_file-input-output")

for filepath in file_location.iterdir():
    #print(filepath)

    if filepath.suffix == ".txt":
        words_file = filepath 

        with open(words_file) as file:
            empty_list = []
            for line in file:
                line_counter = len(file.readlines())         
                print(line_counter)
                print(max(line))
                #line_length = len(line)
                #empty_list.append(line_length)
                #for i in empty_list:
                    #print(max(i))


          










#using a loop to count the number of lines below
#for filepath in file_location.iterdir():
    #print(filepath)
    #if filepath.suffix == ".txt":
        #words_file = filepath 
        #empty_list = []
            #counter = 0
            #for line in file:
            #    line_counter = count(line)
            #    counter = counter + 1
            #    each_word = line.rstrip()
            #    empty_list.append(each_word)
            #    list_lengt = len(empty_list)
        #print(list_lengt)



        
              
                