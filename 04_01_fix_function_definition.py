# The following function definition has a whole lot of bugs in it!
# Run the script and follow Python's error hints to fix them all.
# After your fixes, the function should allow you to take a name as an input
# and return a greeting message that you can save to a variable.

from unicodedata import name

def say_hello(greeting, name):
        return print(f"{greeting}, {name}, how are you?")

say_hello("hey", "ugo")