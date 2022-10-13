# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def say_hello(greeting, name):
        print(f"{greeting}, {name}, how are you?")
        
        def body_of_letter():
                letter_body = (input(""))
                closing = print(f"yours sincerely {name}")
                return body_of_letter, letter_body, "\n", closing

say_hello("Hey", "Ugo")