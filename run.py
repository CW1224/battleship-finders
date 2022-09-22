def accept_game():
    '''
    Function for the user to accept the challenge. 
    Choosing yes would bring the user to the next part of the game. 
    Choosing no means that the user would stay on the same page.
    '''
    print("Would you like to start the game?")
    user_accept = int(input("Press 1 for yes\n"))
    print("")
    
    # Pressing 1 would allow the instruction question to show.
    if user_accept == 1:
        print("Would you like to read the instructions?")
        instructions = int(input("Press 1 for yes, 0 for no\n"))
        print("")
        if instructions == 1:
            show_instructions()
        # Pressing 0 would allow the user to skip the instructions and go straight to the page where the difficulty level is picked.
        else:
            difficulty_level()


def show_instructions():
    '''
    Function that gives the user a choice to read or not read the instructions.
    Choosing yes would allow the user to read the instructions. 
    Choosing no would bring the user to the next part of the game.
    '''
    print("The goal of this game is to sink all of the opponant's ships.")
    print("You will have a choice between grid sizes of 6x6 or 10x10.")
    print("Both players will have a total of four ships.")
    print("You will have a total of 24 bullets.")
    print("Choose where you want to aim by typing in the co-ordinates.")
    print("The co-ordinates should be expressed as x,y.")
    print("An example would be 3,4 .")
    print("The top left of the grid is 1,1 .")
    print("As you go across the grid, the first number(x) increases.")
    print("As you go down the grid, the second number (y) increases.")
    print("The game ends when all the ships have been sank or when your bullet runs out.")
    print("Think carefully and enjoy the game!\n")

    instructions_read = int(input("Press 0 when you have finished reading the instructions.\n"))
    print("")

    if instructions_read == 0:
        difficulty_level()

def difficulty_level():
    print("Which type of challenge are you up for?")
    user_level_choice = int(input("Press 1 for easy and 2 for hard\n"))


print("Welcome to Battleship Attack!\n")

accept_game()