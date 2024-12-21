def display_board(board):
    print("\nCurrent Board State:\n")
    print("    1   2   3")
    for i in range(9):
        if i % 3 == 0:
            if i > 0:
                print("\n  ----|----|---")
            print(f"{(i // 3) + 1} ", end="")
        
        if board[i] == 0:
            print("   ", end=" ")
        elif board[i] == -1:
            print(" X ", end=" ")
        elif board[i] == 1:
            print(" O ", end=" ")
        
        if (i + 1) % 3 != 0:
            print("|", end="")
    print("\n")

def player_x_turn(board):
    while True:
        pos = input("Enter a position for X (1-9): ")
        pos = int(pos)
        if 1 <= pos <= 9 and board[pos - 1] == 0:
            board[pos - 1] = -1
            break
        else:
            print("Invalid move. Try again.")

def player_o_turn(board):
    while True:
        pos = input("Enter a position for O (1-9): ")
        pos = int(pos)
        if 1 <= pos <= 9 and board[pos - 1] == 0:
            board[pos - 1] = 1
            break
        else:
            print("Invalid move. Try again.")

def evaluate_board(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] != 0 and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    return 0

def minimax(board, player):
    winner = evaluate_board(board)
    if winner != 0:
        return winner * player

    best_value = -float('inf')
    best_position = -1

    for i in range(9):
        if board[i] == 0:
            board[i] = player
            value = -minimax(board, -player)
            board[i] = 0
            if value > best_value:
                best_value = value
                best_position = i

    if best_position == -1:
        return 0
    return best_value

def computer_turn(board):
    best_value = -float('inf')
    best_position = -1

    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            value = -minimax(board, -1)
            board[i] = 0
            if value > best_value:
                best_value = value
                best_position = i

    board[best_position] = 1

def main():
    game_mode = input("1. Single player \n2. Multiplayer\n")
    game_mode = int(game_mode)
    board = [0] * 9

    if game_mode == 1:
        print("You (X) vs Computer (O)")
        turn = input("1. For first turn\n2. For second turn\n")
        turn = int(turn)

        for move in range(9):
            if evaluate_board(board) != 0:
                break

            if (move + turn) % 2 == 0:
                computer_turn(board)
            else:
                display_board(board)
                player_x_turn(board)

    else:
        for move in range(9):
            if evaluate_board(board) != 0:
                break

            if move % 2 == 0:
                display_board(board)
                player_x_turn(board)
            else:
                display_board(board)
                player_o_turn(board)

    result = evaluate_board(board)
    display_board(board)
    if result == 0:
        print("It's a draw!")
    elif result == -1:
        print("Player X wins!")
    elif result == 1:
        print("Player O wins!")

main()
