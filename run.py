board = []

for i in range(0,5):
    board.append(["O"]*5)


def print_board(board):
    for i in board:
        print(" ".join(i))

print_board(board)