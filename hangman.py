# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it


the_word = "gold"
empty_word = ["*", "*", "*", "*"]
player1_name = input("what is your name? ")
counter = 0

opening_statement = print(f"""
Welcome to my hangman game! In this game, you have to save your characters life.
You can do this by guessing the right word, letter by letter.The word is case sensitive.
For each guess, you lose a try and you have only 6 tries. If you get a letter correct, it will display below.
If you don't guess any correct letters or the game finishes early, then you lose and your character gets hung.
Your characters name is {player1_name}.  
""")                       

errorr_count = 0

for tries in range(6):
    counter = counter + 1  
    guess = input("guess a letter: ")
    hang_guess = "_ _ _ _"
    findit = the_word.find(guess)                               
    word_finder = the_word[findit]
    the_word2 = " "
    errorr = len(guess) >1
    
    if len(guess) >1:
        errorr_count = errorr_count + 1
        print("ERROR! you can only guess 1 letter at a time")
    
    if errorr_count == 2:
        print("you broke the rules twice. your player gets hung and the game ends now.")
        break   

    if counter == 0:
        continue

    if counter == 1:
        print("you have 5 tries left")

    elif counter == 2:
        print("you have 4 tries left")

    elif counter == 3:
        print("you have 3 tries left")

    elif counter == 4:
        print("you have 2 tries left")

    elif counter == 5:
        print("you have 1 tries left")

    elif counter == 6:
        print("you have run out of tries, and so has your player in the game. the game ends now..")

    if findit == 0:
        empty_word[findit] = "g"
        #print(word_finder, "_ _ _")
        #the_word2 = "g"
        print(empty_word)
        joiner = "".join(empty_word)
        print(joiner)

    elif findit == 1:
        empty_word[findit] = "o"
        #print("_", word_finder, "_ _")
        #the_word2 = "go"
        print(the_word2)
        #print(" ".join(empty_word))
        joiner = "".join(empty_word)
        print(joiner)

    elif findit == 2:
        empty_word[findit] = "l"
        #print("_ _", word_finder, "_")
        #the_word2 = "gol"
        print(the_word2)
        #print(" ".join(empty_word))
        joiner = "".join(empty_word)
        print(joiner)

    elif findit == 3:
        empty_word[findit] = "d"
        #print("_ _ _", word_finder)
        #the_word2 = "gold"
        print(the_word2)
        #print(" ".join(empty_word))
        joiner = "".join(empty_word)
        print(joiner)

    else:
        print("your input is not in the word. keep trying!")
        print(hang_guess)

    if joiner == "gold":
        print("well done! you've saved your characters life! the game ends now..")
        break
    
