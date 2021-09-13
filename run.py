LETTERS = [" ", "A", "B", "C", "D", "E"]
board = []

board.append(LETTERS)
for i in range(0,5):
    board.append([f"{i + 1}"] + ["0"] * 5)


def print_board(board):
    for i in board:
        print(" ".join(i))

def main():
    print_board(board)

main()