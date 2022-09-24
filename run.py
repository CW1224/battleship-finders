from random import randint


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
    print("You will have a choice between grid sizes of 6x6 or 8x8.")
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
    '''
    Function that allows the user to choose between easy and hard.
    There are two choices altogether.
    '''
    while True:
        print("Which type of challenge are you up for?")
        user_level_choice = input("Press 1 for easy and 2 for hard\n")
        answer = "three"

        if initial_validation(user_level_choice, answer):
            break

    user_level_choice = int(user_level_choice)

    # The user would have a choice between the easy and hard game.
    if user_level_choice == 1:
        easy()
    
    elif user_level_choice == 2:
        hard()

grid = []
cpu_grid = []

def easy():
    '''
    Function that generates the easy grid or the 6 x 6 grid.
    This block of code was taken from iKelvvv and modified.
    Reference is given in the readme.
    The original would be pasted there.
    '''
    for x in range(6):
        #Generates the size of the playing board.
        grid.append(["-"] * 6)
        cpu_grid.append(['_'] * 6)
    
    def player_ship_col(grid):
        #Generates a random column's number of the player's ship.
        return randint(0, len(grid) - 1)


    def player_ship_row(grid):
        #Generates a random row's number of the player's ship.
        return randint(0, len(grid) - 1)


    def cpu_ship_col(cpu_grid):
        #Generates a random column's number of the computer's ship.
        return randint(0, len(cpu_grid) - 1)


    def cpu_ship_row(cpu_grid):
        #Generates a random row's number of the computer's ship.
        return randint(0, len(cpu_grid) - 1)

    ship_col = player_ship_col(grid)
    ship_row = player_ship_row(grid)
    cpu_col = cpu_ship_col(cpu_grid)
    cpu_row = cpu_ship_row(cpu_grid)
    
    while True:
        '''
        Loop that doesn't allow the player's or cpu's ship 
        to be generated in the same location.
        '''
        ship_col2 = player_ship_col(grid)
        ship_row2 = player_ship_row(grid)
        cpu_col2 = cpu_ship_col(cpu_grid)
        cpu_row2 = cpu_ship_row(cpu_grid)
        if (ship_col2 != ship_col and ship_row2 != ship_row) and \
        (cpu_col2 != cpu_col and cpu_row2 != cpu_row):
            ship_col3 = player_ship_col(grid)
            ship_row3 = player_ship_row(grid)
            cpu_col3 = cpu_ship_col(cpu_grid)
            cpu_row3 = cpu_ship_row(cpu_grid)
            if (ship_col3 != ship_col2 and ship_row3 != ship_row2) and \
            (ship_col3 != ship_col and ship_row3 != ship_row) and \
            (cpu_col3 != cpu_col2 and cpu_row3 != cpu_row2) and \
            (cpu_col3 != cpu_col and cpu_row3 != cpu_row):
                break

    grid[ship_col][ship_row] = "S"
    grid[ship_col2][ship_row2] = "S"
    grid[ship_col3][ship_row3] = "S"

    print_boards()


def hard():
    # Function that generates the easy grid or the 8 x 8 grid.
    for x in range(8):
        #Generates the size of the playing board.
        grid.append(["-"] * 8)
        cpu_grid.append(['_'] * 8)

    print_boards()


def board_format(board):
    for row in board:
        print(" ".join(row))

def print_boards():
    print("Player's Board:")
    board_format(grid)
    print("")
    print("Computer's Board:")
    board_format(cpu_grid)


# This block of code is taken from Love Sandwiches and modified accordingly.
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