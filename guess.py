# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

corr_num = 28

for tries in range(3):
    guess_game = input("guess my age:___")

    if guess_game == corr_num:
        print("yay")

    elif guess_game != corr_num:
        print("keep trying")
