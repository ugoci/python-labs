# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

mess1 = input("what is your first word?: ")
mess2 = input("what is your second word?: ")
mess3 = input("what is your third word?: ")

user_input = [mess1, mess2, mess3]
longest_string = max(user_input)
if longest_string == mess1:
    print(len(mess1), longest_string)

if longest_string == mess2:
    print(len(mess2), longest_string)

if longest_string == mess3:
    print(len(mess3), longest_string)


