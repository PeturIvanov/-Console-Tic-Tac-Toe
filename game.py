from math import ceil
from colorama import Fore


def setup():
    global player_one_data, player_two_data

    player_one_name = input("Enter first player name: ").title()
    player_two_name = input("Enter second player name: ").title()

    player_one_sign = input(f"\n{player_one_name} choose symbol 'X' or 'O': ").upper()

    while player_one_sign not in "XO":
        print("The sign have to be 'X' or 'O'!")
        player_one_sign = input("Enter valid symbol 'X' or 'O': ").upper()

    player_two_sign = Fore.RED + "X" + Fore.RESET if player_one_sign == "O" else Fore.RED + "O" + Fore.RESET

    player_one_sign = Fore.BLUE + player_one_sign + Fore.RESET

    player_one_data = [player_one_name, player_one_sign]
    player_two_data = [player_two_name, player_two_sign]

    print(f"\n{player_one_name} is with '{player_one_sign}'")
    print(f"{player_two_name} is with '{player_two_sign}'")
    print("\nThis is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |\n")


def play(current, board):
    print(f"{current[0]} is your turn.")

    choice = int(input("Select a empty field [1-9]: "))

    while True:
        if not 0 < choice < 10:
            choice = int(input("Invalid field!\nSelect again: "))
            continue

        r = ceil(choice / 3) - 1
        c = choice % 3 - 1

        if board[r][c] == " ":
            board[r][c] = current[1]
            break

        else:
            choice = int(input("You have to select empty field!\nSelect again: "))

    draw_board(board)
    winner(current_player, board)


def draw_board(board):
    print()
    for row in board:
        print("| ", end="")
        print(" | ".join([x for x in row]), end="")
        print(" |")


def winner(current_player, board):
    global game_on

    first_row = all([x == current_player[1] for x in board[0]])
    second_row = all([x == current_player[1] for x in board[1]])
    third_row = all([x == current_player[1] for x in board[2]])
    first_col = all(x == current_player[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_col = all(x == current_player[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_col = all(x == current_player[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current_player[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current_player[1] for x in [board[0][2], board[1][1], board[2][0]])

    if any([first_row, second_row, third_row, first_col, second_col, third_col, first_diagonal, second_diagonal]):
        print(f"{current_player[0]} win!")
        game_on = False


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

player_one_data = None
player_two_data = None
setup()
current_player = player_one_data
next_player = player_two_data
game_on = True

while game_on:
    play(current_player, board)

    current_player, next_player = next_player, current_player
