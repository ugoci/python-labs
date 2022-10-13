# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

memory_game = True
game_set = []
points = 0

while memory_game:
    user_input = int(input("write a number:"))
    #print(user_input)
    game_set.append(user_input)
    print(game_set)
    occur = game_set.count(user_input)
    print("your score is:", points)
    if occur == 1:
        points = points + 1

    elif occur > 1:
        print("that number is already in the set")
        points = points - 1
        print("your score is:", points)
    
    if points == 0:
        print("you have lost the plot. the game ends now!")
        memory_game = False
