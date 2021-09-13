from random import randint

LETTERS = [" ", "A", "B", "C", "D", "E"]
board = []
coordinates = []

board.append(LETTERS)
for i in range(0,5):
    board.append([f"{i + 1}"] + ["0"] * 5)


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
    message = "How many ships would you like hidden? "
    amount = input(message)
    try:
        amount = int(amount)
    except ValueError:
        message = "Please enter integer values only: "
    else:
        valid = 2 < amount < 7
        if not valid:
            message = "Enter an integer between 3 and 6: "
    for i in range(0, amount):
        add_to_list()
    print(f"{amount} ships hidden. Good luck!")


def player_guess():
    guess = str(input("Guess coordinate: "))
    check_guess(guess)


def check_guess(guess):
    if len(guess) < 2:
        print("Too few characters in coordinate")
        player_guess()
    elif len(guess) > 2:
        print("Too many characters in coordinate")
        player_guess()
    else:
        col = guess[0].capitalize()
        if (col in LETTERS):
            try:
                x = LETTERS.index(col)
            except TypeError:
                print("Invalid coordinate")
        else:
            print("Invalid coordinate.")
            player_guess()


def main():
    print_board(board)
    hide_ships()
    print(coordinates)
    player_guess()


main()