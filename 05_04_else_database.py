# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.


try:
    user_input = int(input("say a number: "))
    calculate = user_input / 3
    print(calculate)

except ValueError:
    print("you have to choose a number")

else:
    if calculate > 10:
        print("this conditional if block runs under the else statement")
    elif calculate < 10 > 0:
        print("this conditional elif block runs under the else statement")

