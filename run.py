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
        user_level_choice = input("Press 1 for easy, 2 for medium and 3 for hard.\n")
        answer = "three"

        if initial_validation(user_level_choice, answer):
            break

    user_level_choice = int(user_level_choice)

    # The user would have a choice between the easy, medium and hard game.
    if user_level_choice == 1:
        game_logic(6,25)
    
    elif user_level_choice == 2:
        game_logic(7,36)

    elif user_level_choice == 3:
        game_logic(8,49)

grid = []
cpu_grid = []

def game_logic(wide,number):
    '''
    Function that generates the easy grid or the 6 x 6 grid.
    This block of code was taken from iKelvvv and modified.
    Reference is given in the readme.
    The original would be pasted there.
    '''
    for x in range(wide):
        #Generates the size of the playing board.
        grid.append(["-"] * wide)
        cpu_grid.append(['-'] * wide)
    
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
    
    #Original position of the player's ships.
    grid[ship_row][ship_col] = "S"
    grid[ship_row2][ship_col2] = "S"
    grid[ship_row3][ship_col3] = "S"

    print_boards()

    '''
    The code below executes the game.
    The player will start with a certain number of bullets depending on difficulty.
    Their aim is to sink all three of the opponent's ships.
    '''
    bullets = number
    ships_remaining = 3
    bullets_used = 0
    co_ordinates_used = []

    while bullets != 0 and ships_remaining != 0:
        '''
        Loop that will continue until the bullet runs out
        or until all ships are sank.
        '''
        while True:
                    
            print("Where do you want to aim?")

            player_input_row = input("Enter the horizontal co-ordinate here\n")
            player_input_col = input("Enter the vertical co-ordinate here\n")

            print(f"The co-ordinate you entered is {player_input_row},{player_input_col}.")
                
            '''
            This statement validates the code.
            Also prevents the same co-ordinate from being entered twice.
            Which also prevents the same ship from being sunk twice.
            '''
            if coordinate_validation(player_input_row,7) and coordinate_validation(player_input_col,7):
                print("Data is valid")
                co_ordinates_entered_alone = [(int(player_input_row),int(player_input_col))]
                co_ordinates_entered = set(co_ordinates_entered_alone)
                print(co_ordinates_used)

                if co_ordinates_entered.issubset(co_ordinates_used):
                    print("You have already entered this co-ordinate.")
                    print("Please try again\n")
                else:
                    co_ordinates_used.extend(co_ordinates_entered)
                    bullets -= 1
                    bullets_used += 1
                    break    

        '''
        This allows the player's co-ordinates to sync with the system's.
        The system's first grid has the co-ordinates (0,0) which is one less than the person's input at (1,1).
        '''
        player_input_row = int(player_input_row) - 1
        player_input_col = int(player_input_col) - 1 

        print(f"Co-ordinates entered: {co_ordinates_used}\n")

        '''    
        This will notify the system that a ship has been sank.
        This would also mark the spot where a ship isn't located.
        '''
        if (player_input_row == cpu_row and player_input_col == cpu_col) \
            or (player_input_row == cpu_row2 and player_input_col == cpu_col2) \
            or (player_input_row == cpu_row3 and player_input_col == cpu_col3):
            cpu_grid[player_input_row][player_input_col] = 'E'
            print("Hit")
            ships_remaining -= 1
        else:
            cpu_grid[player_input_row][player_input_col] = 'X'
            print("You missed")

        if ships_remaining == 0 or bullets == 0:
            break
            
        '''
        The computer's action will do the same thing as the player's.
        The computer should not generate the same co-ordinates.
        The computer's guess will show on the player's board.
        '''
        ships_remaining_cpu = 3

        while True:
            cpu_guess_row = player_ship_row(grid)
            cpu_guess_col = player_ship_col(grid)

            cpu_co_ordinates_used = []
            cpu_co_ordinates_entered_alone = [(int(cpu_guess_row),int(cpu_guess_col))]
            cpu_co_ordinates_entered = set(cpu_co_ordinates_entered_alone)

            if co_ordinates_entered.issubset(cpu_co_ordinates_used):
                continue
            else:
                break

        if (cpu_guess_row == ship_row and cpu_guess_col == ship_col) \
            or (cpu_guess_row == ship_row2 and cpu_guess_col == ship_col2) \
            or (cpu_guess_row == ship_row3 and cpu_guess_col == ship_col3):
            grid[cpu_guess_row][cpu_guess_col] = 'E'
            print("The computer sank your ship")
            ships_remaining_cpu -= 1
        else:
            grid[cpu_guess_row][cpu_guess_col] = 'X'
            print("The computer missed")

        print_boards()

        if ships_remaining_cpu == 0:
            break

    if ships_remaining == 0:
        print(f"Congratulations!\nYou have sank all your opponent's ships with {bullets_used} bullets.\n")
    elif bullets == 0:
        print(f"Too bad!\n You have no more bullets left.\n There are {ships_remaining} ships remaining.\n")
    elif ships_remaining_cpu == 0:
        print(f"The computer has sank all your ships")
        print(f"There are {ships_remaining} ships remaining.")


def board_format(board):
    for row in board:
        print(" ".join(row))


def print_boards():
    print("Player's Board:")
    board_format(grid)
    print("")
    print("Computer's Board:")
    board_format(cpu_grid)
    print("")


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
        elif number_of_answers == 'three' and value!= 1 and value!= 2 and value!=3:
            raise ValueError(
                f"The number you entered is {value}."
            )

    except ValueError as e:
        print(f"Invalid data: {e} Please try again.\n")
        return False

    return True


def coordinate_validation(value,grid_length):
    '''
    Function that checks if the user enters an integer.
    Also checks if the the co-ordinate is valid.
    '''
    try:
        value = int(value)
        if value not in range(grid_length):
            raise ValueError(
                f"The number you entered is {value}. It is not within the length of the board."
            )

    except ValueError as e:
        print(f"Invalid data: {e} Please try again.\n")
        return False

    return True


print("Welcome to Battleship Attack!\n")

accept_game()