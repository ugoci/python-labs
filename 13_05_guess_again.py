# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

from tkinter import END


counter = 0
correct_number = True

while correct_number is True and range(3):
    counter = counter + 1
    guess = input("guess a number: ")
    
    if guess == "28":
        print("well done")
        correct_number = False
        
    else:
        print("keep trying")

    if counter == 3 and correct_number == True:
        print("you're out of tries")
        correct_number = False
    
    elif counter == 3 and correct_number == False:
        print("well done, the game is over!")
        