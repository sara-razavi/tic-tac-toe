# Name: Sara Razavi
# Student ID: 970050118
# Project date: December 17, 2019
# Focus: while loops, lists, functions, conditions

board = [" " for i in range(9)]

def show_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in combinations:
        if board[combo[0]] == player:
            if board[combo[1]] == player and board[combo[2]] == player:
                return True

    return False

def board_full():
    for item in board:
        if item == " ":
            return False
    return True

print("TIC TAC TOE")
print("Player 1 = X")
print("Player 2 = O")

current_player = "X"

while True:
    show_board()

    print("Player", current_player)
    choice = input("Choose a position from 1 to 9: ")

    if not choice.isdigit():
        print("Please enter a number.")
        continue

    position = int(choice) - 1

    if position < 0 or position > 8:
        print("That position does not exist.")
        continue

    if board[position] != " ":
        print("That place is already taken.")
        continue

    board[position] = current_player

    if check_winner(current_player):
        show_board()
        print("Player", current_player, "wins!")
        break

    if board_full():
        show_board()
        print("It is a draw.")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# I used a list for the board to make it easier.
