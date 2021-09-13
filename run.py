from random import randint

LETTERS = [" ", "A", "B", "C", "D", "E"]
board = []

board.append(LETTERS)
for i in range(0,5):
    board.append([f"{i + 1}"] + ["0"] * 5)


def print_board(board):
    for i in board:
        print(" ".join(i))


def random_point(board):
    return randint(1, len(board)-1)


def random_coordinate(board):
    return [random_point(board), random_point(board)]



def main():
    print_board(board)
    r = random_coordinate(board)
    print(r)

main()