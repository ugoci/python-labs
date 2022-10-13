# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

runnit = True 

while runnit == True:
    try:
        user_input = int(input("choose first number: "))
        user_input2 = int(input("chose second number: "))
        coetient = user_input * user_input2
        print(coetient)
    
    except:
        print("you have to chose a number")

