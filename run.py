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
        if initial_validation(user_accept, answer):
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
            if initial_validation(instructions, answer):
                break

        instructions = int(instructions)

        if instructions == 1:
            show_instructions()
        # Inserting 0 allows user to go straight to difficulty choice.
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
    print("You will have a limited number of bullets.")
    print("Choose where you want to aim by typing in the co-ordinates.")
    print("The co-ordinates should be expressed as x,y.")
    print("An example would be 3,4 .")
    print("The top left of the grid is 1,1 .")
    print("As you go across the grid, the first number(x) increases.")
    print("As you go down the grid, the second number (y) increases.")
    print("The game ends when the bullets run out or when all ships are sank")
    print("Think carefully and enjoy the game!\n")

    while True:
        # Determining if the answer the user inputs is valid or not.
        instructions_read = input("Press 1 when you have finished.\n")
        answer = 'one'
        print("")

        if initial_validation(instructions_read, answer):
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
        print("Which type of challenge are you up for?\n")
        print("Press 1 for the easy grid, 2 for medium")
        print("3 for hard and 4 for impossible.")
        user_level_choice = input("Insert 1, 2, 3 or 4.\n")
        answer = "four"

        if initial_validation(user_level_choice, answer):
            break

    user_level_choice = int(user_level_choice)

    # The user would have a choice between the four different grid sizes.
    if user_level_choice == 1:
        game_logic(5, 20)

    elif user_level_choice == 2:
        game_logic(6, 30)

    elif user_level_choice == 3:
        game_logic(7, 40)

    elif user_level_choice == 4:
        game_logic(8, 49)


grid = []
cpu_grid = []


def game_logic(wide, number):
    '''
    This block of code was taken from iKelvvv and modified.
    Reference is given in the readme.
    The original would be pasted there.
    '''
    for x in range(wide):
        # Generates the size of the playing board.
        grid.append(["-"] * wide)
        cpu_grid.append(['-'] * wide)

    def player_ship_col(grid):
        # Generates a random column's number of the player's ship.
        return randint(0, len(grid) - 1)

    def player_ship_row(grid):
        # Generates a random row's number of the player's ship.
        return randint(0, len(grid) - 1)

    def cpu_ship_col(cpu_grid):
        # Generates a random column's number of the computer's ship.
        return randint(0, len(cpu_grid) - 1)

    def cpu_ship_row(cpu_grid):
        # Generates a random row's number of the computer's ship.
        return randint(0, len(cpu_grid) - 1)

    ship_col = player_ship_col(grid)
    ship_row = player_ship_row(grid)
    cpu_col = cpu_ship_col(cpu_grid)
    cpu_row = cpu_ship_row(cpu_grid)

    # Loop that doesn't allow ship to be placed at same space.
    while True:
        # The second ship's position
        ship_col2 = player_ship_col(grid)
        ship_row2 = player_ship_row(grid)
        cpu_col2 = cpu_ship_col(cpu_grid)
        cpu_row2 = cpu_ship_row(cpu_grid)
        # The second ship's position's check
        if (ship_col2 != ship_col and ship_row2 != ship_row) and \
           (cpu_col2 != cpu_col and cpu_row2 != cpu_row):
            # The third ship's position
            ship_col3 = player_ship_col(grid)
            ship_row3 = player_ship_row(grid)
            cpu_col3 = cpu_ship_col(cpu_grid)
            cpu_row3 = cpu_ship_row(cpu_grid)
            # The third ship's position's check
            if (ship_col3 != ship_col2 and ship_row3 != ship_row2) and \
               (ship_col3 != ship_col and ship_row3 != ship_row) and \
               (cpu_col3 != cpu_col2 and cpu_row3 != cpu_row2) and \
               (cpu_col3 != cpu_col and cpu_row3 != cpu_row):
                # The fourth ship's position
                ship_col4 = player_ship_col(grid)
                ship_row4 = player_ship_row(grid)
                cpu_col4 = cpu_ship_col(cpu_grid)
                cpu_row4 = cpu_ship_row(cpu_grid)
                # The fourth ship's position's check
                if (ship_col4 != ship_col3 and ship_row4 != ship_row3) and \
                   (ship_col4 != ship_col2 and ship_row4 != ship_row2) and \
                   (ship_col4 != ship_col and ship_row4 != ship_row) and \
                   (cpu_col4 != cpu_col3 and cpu_row4 != cpu_row3) and \
                   (cpu_col4 != cpu_col2 and cpu_row4 != cpu_row2) and \
                   (cpu_col4 != cpu_col and cpu_row4 != cpu_row):
                    break

    # Original position of the player's ships.
    grid[ship_row][ship_col] = "S"
    grid[ship_row2][ship_col2] = "S"
    grid[ship_row3][ship_col3] = "S"
    grid[ship_row4][ship_col4] = "S"

    print_boards()

    # Code that allows the game to be played.
    bullets = number
    ships_remaining = 4
    bullets_used = 0
    co_ordinates_used = []

    # Loop to continue until statements fulfilled.
    while bullets != 0 and ships_remaining != 0:
        while True:

            print("Where do you want to aim?")

            player_input_row = input("Enter the horizontal co-ordinate here\n")
            player_input_col = input("Enter the vertical co-ordinate here\n")

            print(f"You entered: {player_input_row},{player_input_col}.")

            # This statement validates the code.
            if coordinate_validation(player_input_row, 7) and \
               coordinate_validation(player_input_col, 7):
                co_ordinates = [(int(player_input_row), int(player_input_col))]
                co_ordinates_entered = set(co_ordinates)

                # Prevents the same co-ordinate from being entered twice.
                if co_ordinates_entered.issubset(co_ordinates_used):
                    print("You have already entered this co-ordinate.")
                    print("Please try again\n")
                else:
                    co_ordinates_used.extend(co_ordinates_entered)
                    bullets -= 1
                    bullets_used += 1
                    break

        # This allows the player's co-ordinates to sync with the system's.
        # (1,1) for player and (0,0) for system are in the same place.
        player_input_row = int(player_input_row) - 1
        player_input_col = int(player_input_col) - 1

        print(f"Co-ordinates entered: {co_ordinates_used}\n")

        # This will notify the system that a ship has been sank.
        if (player_input_row == cpu_row and player_input_col == cpu_col) \
           or (player_input_row == cpu_row2 and player_input_col == cpu_col2)\
           or (player_input_row == cpu_row3 and player_input_col == cpu_col3)\
           or (player_input_row == cpu_row4 and player_input_col == cpu_col4):
            cpu_grid[player_input_row][player_input_col] = 'E'
            print("Hit")
            ships_remaining -= 1
        else:  # This would also mark the spot where a ship isn't located.
            cpu_grid[player_input_row][player_input_col] = 'X'
            print("You missed")

        if ships_remaining == 0 or bullets == 0:
            break

        # The computer's action are the same thing as the player's.
        ships_remaining_cpu = 4

        while True:
            cpu_guess_row = player_ship_row(grid)
            cpu_guess_col = player_ship_col(grid)

            cpu_co_ordinates_used = []
            cpu_co_ordinates_alone = [(int(1), int(2))]
            cpu_co_ordinates_entered = set(cpu_co_ordinates_alone)

            # The computer should not generate the same co-ordinates.
            if cpu_co_ordinates_entered.issubset(cpu_co_ordinates_used):
                continue
            else:
                break

        # The computer's guess will show on the player's board.
        if (cpu_guess_row == ship_row and cpu_guess_col == ship_col) \
           or (cpu_guess_row == ship_row2 and cpu_guess_col == ship_col2) \
           or (cpu_guess_row == ship_row3 and cpu_guess_col == ship_col3) \
           or (cpu_guess_row == ship_row4 and cpu_guess_col == ship_col4):

            # An e for a correct guess.
            grid[cpu_guess_row][cpu_guess_col] = 'E'
            print("The computer sank your ship")
            ships_remaining_cpu -= 1
        else:  # An x for an incorrect guess.
            grid[cpu_guess_row][cpu_guess_col] = 'X'
            print("The computer missed")

        print_boards()

        if ships_remaining_cpu == 0:
            break

    if ships_remaining == 0:
        print("Congratulations!")
        print("You have sank all your opponent's ships")
        print(f"with {bullets_used} bullets.\n")
    elif bullets == 0:
        print("Too bad!")
        print("You have no more bullets left.")
        print(f"There are {ships_remaining} ships remaining.\n")
    elif ships_remaining_cpu == 0:
        print("The computer has sank all your ships")
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
def initial_validation(value, number_of_answers):
    '''
    The function that would determine if the data entered is valid or not.
    Depending on the number of answers, one of the function below would apply.
    '''
    try:
        value = int(value)
        if number_of_answers == 'two' and value != 0 and value != 1:
            raise ValueError(
                f"The number you entered is {value}. Enter with 0 or 1."
            )
        elif number_of_answers == 'one' and value != 1:
            raise ValueError(
                f"The number you entered is {value}. Enter with 1."
            )
        elif (
            number_of_answers == 'four' and
            value != 1 and
            value != 2 and
            value != 3 and
            value != 4
        ):
            raise ValueError(
                f"You have entered {value}. Enter with 1, 2, 3 or 4."
            )

    except ValueError as e:
        print(f"Invalid data: {e} Please try again.\n")
        return False

    return True


def coordinate_validation(value, grid_length):
    '''
    Function that checks if the user enters an integer.
    Also checks if the the co-ordinate is valid.
    '''
    try:
        value = int(value)
        if value not in range(grid_length):
            raise ValueError(
                f"You have entered {value}.\n It is not within the range.")

    except ValueError as e:
        print(f"Invalid data: {e} Please try again.\n")
        return False

    return True


print("Welcome to Battleship Attack!\n")

accept_game()
