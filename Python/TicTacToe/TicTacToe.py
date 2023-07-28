# What You Will Create
# Create a TicTacToe game in python, where two users can play together.

# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.


def display_board(board):
    print("-TIC TAC TOE-")
    print("**1***2***3**    -  Columns")
    for row in board:
        print("* "  + row[0] + " | " + row[1] + " | " + row[2] + " *")
        print("*---|---|---*")
    print("*************")


def get_player_turn(turn_count):
    if turn_count % 2 == 1:
        return 'X'
    else:
        return 'O'


def get_user_input():
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter values between 1 and 3.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter integer values between 1 and 3.")
# try: and except: are a way to handle errors in a more controlled way than simply letting the program crash.

def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid row/column value.")
        return False
    elif board[row][col] != ' ':
        print("This position is already taken.")
        return False
    else:
        return True


def make_move(board, row, col, player):
    board[row][col] = player


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None


def play_game():
    board = [ 
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    turn_count = 1
    while turn_count <= 9:
        display_board(board)
        player = get_player_turn(turn_count)
        print(f"Player {player}'s turn.")
        row, col = get_user_input()
        if is_valid_move(board, row, col):
            make_move(board, row, col, player)
            winner = check_winner(board)
            if winner:
                display_board(board)
                print(f"Player {winner} wins!")
                return
            turn_count += 1
        else:
            continue
    display_board(board)
    print("It's a tie!")

play_game()





    

