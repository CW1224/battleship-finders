def accept_game():
    '''
    Function for the user to accept the challenge. 
    Choosing yes would bring the user to the next part of the game. 
    Choosing no means that the user would stay on the same page.
    '''
    while True:
        print("Would you like to start the game?")
        user_accept = input("Press 1 for yes\n")
        answer = 'one'
        
        print("")

        # Determining if the answer the user imputs is valid or not.
        if initial_validation(user_accept,answer):
            break
    
    user_accept = int(user_accept)

        # Pressing 1 would allow the instruction question to show.
    if user_accept == 1:
        while True:
            print("Would you like to read the instructions?")
            instructions = input("Press 1 for yes, 0 for no\n")
            answer = 'one_zero'
            print("")

            # Determining if the answer the user imputs is valid or not.
            if initial_validation(instructions,answer):
                break

        instructions = int(instructions)
        
        if instructions == 1:
            show_instructions()
    # Pressing 0 would allow the user to skip the instructions and go straight to the page where the difficulty level is picked.
        elif instructions == 0:
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

    while True: 
        # Determining if the answer the user imputs is valid or not.
        instructions_read = input("Press 1 when you have finished reading the instructions.\n")
        answer = 'one'
        print("")

        if initial_validation(instructions_read,answer):
            break
    
    instructions_read = int(instructions_read)

    if instructions_read == 1:
        difficulty_level()


def difficulty_level():
    while True:
        print("Which type of challenge are you up for?")
        user_level_choice = input("Press 1 for easy and 2 for hard\n")
        answer = "three"

        if initial_validation(user_level_choice, answer):
            break

        user_level_choice = int(user_level_choice)
# This block of code is taken from Love Sandwiches and modified accordingly. The code below is the original.
'''
def validate_data(values):

    try: 
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
        
    except ValueError as e:
        print(f"Invalid Data: {e}, please try again\n")
        return False

    return True
'''

def initial_validation(value,number_of_answers):
    '''
    The function that would determine if the data entered is valid or not.
    Depending on the number of answers, one of the function below would apply.
    '''
    try:
        value = int(value)
        if number_of_answers == 'two' and value != 0 and value!= 1:
            raise ValueError(
                f"The number you entered is {value}."
            )
        elif number_of_answers == 'one' and value!= 1:
            raise ValueError(
                f"The number you entered is {value}."
            )
        elif number_of_answers == 'three' and value!= 1 and value!=2:
            raise ValueError(
                f"The number you entered is {value}."
            )

    except ValueError as e:
        print(f"Invalid data: {e} Please try again.\n")
        return False

    return True


print("Welcome to Battleship Attack!\n")

accept_game()
