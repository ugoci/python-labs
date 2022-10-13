#Rock-Paper-Scissors Game
#Code a game of rock paper scissors.
#Instructions
#take in a number 0-2 from the user that represents their hand
#generate a random number 0-2 to use for the computer's hand
#call the function get_hand to get the string representation of the user's hand
#call the function get_hand to get the string representation of the computer's hand
#call the function determine_winner to figure out who won
#print out the player hand and computer hand
#print out the winner
#Some Tips
#Creating a function that gets a "hand" based on a number.
#The function should take in a number and return the string representation of the hand. E.g.:

import random

def get_hand():
    #game = True
    #while game == True:
        try:
            user_hand = int(input("choose a number between 0 and 2 (both inclusive): "))
            computer_hand = random.randint(0,2)
        
        except ValueError:
            print("you have to choose a _number_ between 0 and 2")

        except TypeError:
            print("you can't chose a letter")

        else:
            if user_hand == 0:
                print("user hand: rock")
            elif user_hand == 1:
                print("user hand: paper")
            elif user_hand == 2:
                print("user hand: scissors")
            if computer_hand == 0:
                print("computer hand: rock")
            elif computer_hand == 1:
                print("computer hand: paper")
            elif computer_hand == 2:
                print("computer hand: scissors")
            return [user_hand, computer_hand]

def determine_winner():
    try:
        player_hands_list = get_hand()    
        user_hand = player_hands_list[0]
        computer_hand = player_hands_list[1]
    
    except ValueError:
        print("value error")

    except TypeError:
        print("type error")

    else:
        if user_hand == 0 and computer_hand == 0:
            print("rock to rock is equal")
        elif user_hand == 1 and computer_hand == 1:
            print("paper to paper is equal")
        elif user_hand == 2 and computer_hand == 2:
            print("scissors to scissors is equal")
        elif user_hand == 0 and computer_hand == 1:
            print("paper beats rock, computer wins")
        elif user_hand == 0 and computer_hand == 2:
            print("rock beats scissors, user wins")
        elif user_hand == 1 and computer_hand == 0:
            print("paper beats rock, computer wins")
        elif user_hand == 1 and computer_hand == 2:
            print("scissors beats paper, computer wins")
        elif user_hand == 2 and computer_hand == 0:
            print("rock beats scissors, computer wins")
        elif user_hand == 2 and computer_hand == 1:
            print("scissors beats paper, user wins")
        return "game over"

determine_winner()


















"""#class RockPaperScissors():

#    def __init__(self, user_hand, computer_hand):
#        self.user_hand = user_hand
#        self.computer_hand = computer_hand
        
    def get_hand():
        user_hand = input("choose a number between 0 and 2 (both inclusive): ")
        print(f"user hand: {user_hand}")
        computer_hand = random.randint(0,2)
        print(f"computer hand: {computer_hand}")

    def determine_winner():
        return print("game on")
        #paper beats rock 
        #scissors beat paper 
        #rock and rock is tie 
        #paper and paper is tie 
        #schissors and scissors is tie
        #rock beat scissors 


    get_hand()
    determine_winner()
"""


