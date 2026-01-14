def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("🎮 Tic Tac Toe Game")
    display_board([str(i+1) for i in range(9)])

    for turn in range(9):
        move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Position already taken. Try again.")
            continue

        display_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print("🤝 It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
