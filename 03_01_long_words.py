# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
import csv
import pathlib
from unicodedata import name

file_location = pathlib.Path("C:/Users/Ugo/Documents/School/Studying/Software Development/Coding Nomads/Python 201/03_file-input-output")

for filepath in file_location.iterdir():
    print(filepath)

    if filepath.suffix == ".txt":
        words_file = filepath 

        with open(words_file) as file:
            for line in file:
                each_word = line.rstrip()
                if len(each_word) > 20:
                    print(each_word)
    