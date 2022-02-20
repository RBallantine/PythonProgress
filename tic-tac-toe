"""
    Tic-Tac-Toe
    Ronan Ballantine
    20/02/2022
"""

board_game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player1 = 'X'
player2 = 'Y'
current_player = player2
game = True


# Clears the board to start again
def clear_board():
    return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Restarts the game when won
def restart():
    play_again = ''
    while not (play_again == 'Y' or play_again == 'N'):
        play_again = input("\n\nWould you like to play again? Y/N: ").upper()

    if play_again == 'Y':
        return True
    else:
        return False


# Displays the Tic-Tac-Toe board
def display(board):
    print('\n' * 3)
    print('  ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + '  ')
    print('-------------')
    print('  ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + '  ')
    print('-------------')
    print('  ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + '  ')


# Retrieves player's position selection
def select_position():
    position = 0
    while position not in range(1, 10):
        position = int(input('\nPlease choose a position (1-9): '))

    return position


# Updates board with players new position
def update_board(position, player):
    board_game[position - 1] = player


# Alternates player turn
def change_player(player):
    if player == player1:
        player = player2
    else:
        player = player1

    return player


# Checks if selected position is free
def position_check(board, position):
    return board[position-1] == ' '


# Checks if a player has won the game
def winner_check(board, marker):
    if ((board[6] == marker and board[7] == marker and board[8] == marker) or      # Top row
            (board[6] == marker and board[4] == marker and board[2] == marker) or  # Diagonal
            (board[6] == marker and board[3] == marker and board[0] == marker) or  # Left side
            (board[3] == marker and board[4] == marker and board[5] == marker) or  # Across the middle
            (board[0] == marker and board[1] == marker and board[2] == marker) or  # Across the bottom
            (board[0] == marker and board[4] == marker and board[8] == marker) or  # Diagonal
            (board[2] == marker and board[5] == marker and board[8] == marker) or  # Right side
            (board[1] == marker and board[4] == marker and board[7] == marker)):   # Up the middle

        print(f"\n\n***** CONGRATULATIONS {marker}'s WON *****")
        return False
    else:
        return True


# Checks if the board is full
def full_board(board):
    for space in board:
        if space == ' ':
            return False
        else:
            pass

    print("\n**** Draw ****")

    return True

while (game):

    # Changes player turn
    current_player = change_player(current_player)

    check = False
    # Select position and ensure position is not occupied
    while not check:
        # Retrieves player position selection
        new_position = select_position()
        # Checks if position is free
        check = position_check(board_game, new_position)
        if check:
            # Updates new markers on the board
            update_board(new_position, current_player)
        else:
            print("\nPosition taken!")

    # Displays updated board
    display(board_game)

    # Checks if the board is full or a player has won
    if full_board(board_game):
        replay = False
    else:
        replay = winner_check(board_game, current_player)

    # Asks to restart game if a player has won
    if not replay:
        game = restart()
        if game:
            # Clears board
            board_game = clear_board()
    else:
        pass
