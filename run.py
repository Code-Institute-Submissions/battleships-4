from random import randint
import sys

LETTERS = [" ", "A", "B", "C", "D", "E"]
board = []
coordinates = []
used = []

board.append(LETTERS)
for i in range(0,5):
    board.append([f"{i + 1}"] + ["O"] * 5)


def print_board(board):
    for i in board:
        print(" ".join(i))


def random_int(board):
    return randint(1, len(board)-1)


def random_point():
    point = int(str(random_int(board)) + str(random_int(board)))
    return point


def add_to_list():
    r = random_point()
    if (r in coordinates):
        add_to_list()
    else:
        coordinates.append(r)


def hide_ships():
    while True:
        amount = input("How many ships would you like hidden? ")
        try:
            amount = int(amount)
        except ValueError:
            print("Please enter a number between 3 and 6: ")
            continue
        if 3 <= amount <= 6:
            for i in range(0, amount):
                add_to_list()
            print(f"{amount} ships hidden. Good Luck!")
            break
        else:
            print("Please enter a number between 3 and 6: ")


def player_guess():
    guess = str(input("Guess coordinate: "))
    check_length(guess)
    check_col(guess)
    check_row(guess)
    number = str(LETTERS.index(guess[0].capitalize())) + guess[1]
    number = int(number)
    shot = [LETTERS.index(guess[0].capitalize()), int(guess[1])]
    check_hit(number, shot)


def check_length(guess):
    if len(guess) < 2:
        print("Too few characters in coordinate")
        player_guess()
    elif len(guess) > 2:
        print("Too many characters in coordinate")
        player_guess()
    else:
        pass


def check_col(guess):
    col = guess[0].capitalize()
    if (col in LETTERS):
        try:
            x = LETTERS.index(col)
            return x
        except TypeError:
            print("Invalid coordinate")
    else:
        print("Invalid coordinate.")
        player_guess()


def check_row(guess):
    row = int(guess[1])
    if not 1 <= row < 6:
        print("Invalid coordinate")
        player_guess()
    else:
        pass


def check_win():
    if (coordinates == []):
        print("You sank my battleships!")
        print("Congratulations!")
        replay()


def replay():
    print("Would you like to play again? Y/N")
    replay = input()
    if replay.capitalize() == "Y":
        main()
    elif replay.capitalize() == "N":
        sys.exit()
    else:
        print("Input not recognised, try again.")
        replay()


def check_hit(number, shot):
    if (number in coordinates):
        print("Hit!")
        coordinates.remove(number)
        print(coordinates)
        used.append(number)
        board[shot[1]][shot[0]] = "X"
        check_win()
        print_board(board)
        player_guess()
    else:
        print("Miss!")
        used.append(number)
        board[shot[1]][shot[0]] = "0"
        print_board(board)
        player_guess()


def main():
    print_board(board)
    hide_ships()
    print(coordinates)
    player_guess()


main()