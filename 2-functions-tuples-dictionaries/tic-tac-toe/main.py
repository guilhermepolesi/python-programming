# Your task is to write a simple program that pretends to play tic-tac-toe with the user.
# To make things easier for you we decided to simplify the game. Here are our assumptions:
#
# the computer (i.e. your program) must play using 'X's;
# the user (e.g. you) must play using 'O's;
# the first move belongs to the computer - it always places its first 'X' in the middle of the board;
# all squares are numbered line by line starting with 1 (see session example below for reference)
# the user enters his move by informing the number of the square he chooses – the number must be valid
# that is, it must be an integer, it must be greater than 0 and less than 10, and cannot point to a field
# that is already occupied ;
# the program checks whether the game is over - there are four possible verdicts: the game must continue
# or the game ends in a draw, your victory or the computer's victory;
# the computer responds with its movement and the check is repeated;
# Don't implement any form of artificial intelligence – a random field choice made by the computer is good
# enough for the game.

# the board must be stored as a list of three elements, while each element is another list of three elements
# (the internal lists represent rows) so that all squares can be accessed using the following syntax:
#
# board[row][column]
#
#
# each of the elements of the internal list can contain 'O', 'X', or a digit representing the number of the square
# (such a square is considered free)


import random


def display_board(board):
    print(f'''
                +-------+-------+-------+
                |       |       |       |
                |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
                |       |       |       |
                +-------+-------+-------+
                |       |       |       |
                |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
                |       |       |       |
                +-------+-------+-------+
                |       |       |       |
                |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
                |       |       |       |
                +-------+-------+-------+
                '''
          )


def enter_move(board):
    valid_move = False
    while not valid_move:
        move = input("Enter your move: ")
        valid_move = check_play(board, move)

    display_board(board)


def next_move(board):
    if check_win(board, 'O'):
        print("You won!")
        return False

    if check_win(board, 'X'):
        print("Computer won!")
        return False
    return True


def valid_input(board, move):
    if not move.isdigit():
        return False

    move = int(move)
    if 0 < move < 10:
        valid_move = check_valid_field(board, move)
        if valid_move:
            insert_move_user(board, move)
            return True
    return False


def check_valid_field(board, move):
    move -= 1
    row = move // 3
    column = move % 3
    if board[row][column] != 'X' and board[row][column] != 'O':
        return True
    return False


def check_win(board, player):
    for row in board:
        if all(element == player for element in row):
            return True

    for column in range(3):
        if all(board[row][column] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_play(board, move):
    if valid_input(board, move):
        return True
    print("Invalid move! Enter a valid number in the field")
    return False


def insert_move_user(board, move):
    move -= 1
    row = move // 3
    column = move % 3
    board[row][column] = 'O'


def insert_move_computer(board, move):
    move -= 1
    row = move // 3
    column = move % 3
    board[row][column] = 'X'


def computer_movie(board):
    move = None
    valid_move = False
    while not valid_move:
        move = random.randint(1, 9)
        valid_move = check_valid_field(board, move)

    insert_move_computer(board, move)
    display_board(board)


def play_game(board):
    count = 0
    playing = True
    display_board(board)
    while playing:
        if count == 8:
            print("Draw")
            break
        enter_move(board)
        playing = next_move(board)
        if not playing:
            break
        count += 1
        computer_movie(board)
        playing = next_move(board)
        if not playing:
            break
        count += 1


board = [["1", "2", "3"],
         ["4", "X", "6"],
         ["7", "8", "9"]]

play_game(board)