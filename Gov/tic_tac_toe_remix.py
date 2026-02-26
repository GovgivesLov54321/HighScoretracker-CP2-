# GNB - Tic Tac Toe Remix osns

import random


def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def get_human_move(board):
    while True:
        choice = input("Choose a spot (1-9): ")

        if not choice.isdigit():
            print("Enter a number 1-9.")
            continue

        choice = int(choice)

        if 1 <= choice <= 9:
            if board[choice - 1] not in ["X", "O"]:
                return choice - 1
            else:
                print("Spot already taken.")
        else:
            print("Choose between 1 and 9.")


def get_ai_move(board):
    print("Computer is choosing...")
    available = [i for i in range(9) if board[i] not in ["X", "O"]]
    return random.choice(available)


def play_game():

    print("Welcome to Tic Tac Toe!")

    mode = input("1 Player or 2 Player? (1 or 2): ").strip()

    board = [str(i) for i in range(1, 10)]

    # Coin flip
    coin = random.choice(["H", "T"])
    user_call = input("Coin flip! Choose H or T: ").strip().upper()

    if user_call == coin:
        current_player = "X"
        print("You won the coin flip! X goes first.")
    else:
        current_player = "O"
        print("You lost the coin flip! O goes first.")

    game_over = False

    while not game_over:
        display_board(board)

        # 2 player mode
        if mode == "2":
            print(f"Player {current_player}'s turn")
            move = get_human_move(board)

        # 1 player mode
        elif mode == "1":
            if current_player == "X":
                print("Your turn (X)")
                move = get_human_move(board)
            else:
                move = get_ai_move(board)

        else:
            print("Invalid mode. Defaulting to 2 Player.")
            move = get_human_move(board)

        board[move] = current_player

        # Check win
        if check_win(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            game_over = True
            continue

        # Check tie
        if all(space in ["X", "O"] for space in board):
            display_board(board)
            print("It's a tie!")
            game_over = True
            continue

        # Switch player
        current_player = "O" if current_player == "X" else "X"

play_game()

#Return info of score of player one & player two if the game was two player; and also score of player one if it's a one player game and true/false if they played against a computer (aka it was a one player game); and btw, score = how many wins they get before they exit out the game; also gotta change it up so it asks (even after a win/loss) if they wanna play again or exit and go back to main menu (osns) -- This was 26/02/2026 at approximately 9:48am - bouta smash a maths test innit