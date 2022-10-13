# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib
from tkinter import END

file_location = pathlib.Path("C:/Users/Ugo/Documents/School/Studying/Software Development/Coding Nomads/Python 101")

for filepath in file_location.iterdir():
    print(filepath)
    for file in filepath.iterdir():
        print(" ", file)
    