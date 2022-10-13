# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.
import pathlib

file_name = 'integers.txt'

file_location = pathlib.Path("C:/Users/Ugo/Documents/School/Studying/Software Development/Coding Nomads/Python 301/05_exceptions")

for file_path in file_location.iterdir():
    if file_path.suffix == ".txt":
        open_file = open(file_path, "r")
        line_one = open_file.readlines(1)
        workable_line_one = int("".join(line_one))
        print(line_one)
        calculations_1 = workable_line_one + 1 
        calculations_2 = workable_line_one + 1 * 800 - 6 + 2000 / 3
        print(calculations_1)
        print(calculations_2)

        






