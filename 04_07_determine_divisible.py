# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


def divisible_or(number):
    if number % 4 == 0:
        number = True
    elif number % 7 == 0:
        number = True
    else:
        number = False
    return print(number)

#divisible_or(0)
    
def divisible_and(number_again):
    if number_again % 4 and 7 == 0:
        number_again = True
    else:
        number_again = False
    return print(number_again)

#divisible_and(0)

#user_input = int(input("chose a number:"))

for i in range(3):
    user_input = int(input("chose a number:"))
    yakata = divisible_or(i)
    boomshakalaka = divisible_and(i) 
    