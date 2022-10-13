# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

runnit = True 

while runnit == True:
    user_input = int(input("choose a number: "))

    try:
        #user_input = int(input("choose a number: "))
        if type(user_input) == int:
            print("well done")
            runnit = False
                
    except:
        print("you have to chose a number")









