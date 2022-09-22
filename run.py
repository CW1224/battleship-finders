def accept_game():
    '''
    Function for the user to accept the challenge. 
    Choosing yes would bring the user to the next part of the game. 
    Choosing no means that the user would stay on the same page.
    '''
    print("Would you like to start the game?")
    user_accept = input("Press 1 for yes, press 0 for no\n")
    
    if user_accept == 1:
        show_instructions()


print("Welcome to Battleship Attack!\n")


def main():
    accept_game()