# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

num_month = int(input("input a number to find out what month it represents: "))

while num_month:
    months = ["no month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    assigning_mont = months[num_month]
    print(assigning_mont)
    break

