# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon. 
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.


continue_game = True
sword = False


comm_game1 = (input(str("what is your name: ")))

while continue_game:
    welcome_message = print(f"Hello {comm_game1}, welcome to my command line, role playing game.")
    user_input = input("You are now in the main entry room of the game. As part of this game, you have to choose between Left Door and Right Door. Which door do you choose? Left or Right?: ")

    if user_input == "Right":
        user_input = input("You open the door and go into the room. But look out, there is a Dragon in the room. If you stay, you fight the Dragon. Do you want to go back to the main room? Yes or No?: ")
        if user_input == "Yes":
            user_input = input("You open the door and go back to the main room, but you have to chose a door again. which door do you choose? Left or Right: ")
            if user_input == "Right":
                print("you are back in the room with the dragon again, but since you came here before, the dragon was ready and waiting. you get eaten immediately and lose the game")
                continue_game = False
        elif user_input == "No" and sword == False:
            print("You face the dragon and lose.")
            continue_game = False
        elif user_input == "No" and sword == True:
            print("you face the dragon and win!")
            continue_game = False

    elif user_input == "Left":
        user_input = input("You open the door and go into the room. This is an empty room. Do you want to look around the empty room? Yes or No?: ")
        if user_input == "Yes": 
            user_input = input("You have discovered a sword in the empty room. Do you want to pick up the sword? Yes or No?: ")
            if user_input == "Yes":
                sword = True
                user_input = input("you pick up the sword and go back to the main room. Which door do you chose? Left or Right:")
                if user_input == "Right" and sword == True:
                    print("you face the dragon and win because you have a sword")
                    continue_game = False
                elif user_input == "Right" and sword == False:
                    print("you face the dragon and lose because you don't have a sword")
                    continue_game = False
                elif user_input == "Left" and sword == True:
                    print("this is room is empty becuase you already piicked up the sword. you are automatically teleported to the room with the dragon where you kill it with your sword and win.")
                    continue_game = False
                elif user_input == "Left" and sword == False:
                    user_input = input("You open the door and go into the room. This is an empty room. Do you want to look around the empty room? Yes or No?: ")
                    if user_input == "Yes":
                        sword = True
                        print("you see a sword in the empty room that you missed the last time. you finally have a sword to face the dragon and are automatically teleported back to the room with the dragon where you fight and win.")
                        continue_game = False
                    elif user_input == "No":
                        print("you are automatically teleported back to the room with the dragon and get eaten. you lose!")
                        continue_game = False
            elif user_input == "No":
                user_input == input("you have to go back to the main room. which door do you choose? Left or Right?: ")
                if user_input == "Right": #and sword == True:
                    print("you open the door to the dragon, and you lose because you don't have the sword.")
                    continue_game = False
                elif user_input == "Left":
                    user_input = input("You open the door and go into the room. This is an empty room. Do you want to look around the empty room? Yes or No?: ")
                    if user_input == "Yes":
                        user_input = input("You have discovered a sword in the empty room. Do you want to pick up the sword? Yes or No?: ")
                        if user_input == "Yes":
                            print("you pick up the sword are thrown back into the room with the dragon, but you win because you have the sword.")
                            continue_game = False
                        elif user_input == "No":
                            print("you are thrown back into the room with the dragon and lose because you don't have a sword")
                            continue_game = False
                    elif user_input == "No":
                        print("you are thrown back into the room with the dragon and you lose because you don't have a sword")
                        continue_game = False
        elif user_input == "No":
            print("you are thrown back into the room with the dragon and lose because you don't have a sword")
            continue_game = False

    if user_input == "Quit":
        print("!!!GAME QUIT!!!")
        continue_game = False


