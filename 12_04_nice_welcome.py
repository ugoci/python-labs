# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

user_name = str(input("what is your name?: "))

while user_name:
    alluser_names = user_name.split()
    first_name = alluser_names[0]
    print("hi there", first_name, "you are welcome to this program" )
    break
