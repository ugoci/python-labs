# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter (greeting, name):
    opening = print(f"{greeting} {name}")
    letter_body = (input(""))
    closing = print(f"yours sincerely {name}")
    return opening, "\n", letter_body, "\n", closing

write_letter("Hey", "Ugo")