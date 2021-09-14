from random import randint
import sys

LETTERS = [" ", "A", "B", "C", "D", "E"]
board = []
coordinates = []
used = []


def initialise():
    """
    Resets the board and used coordinate lists for a new round
    """
    board.clear()
    used.clear()


def create_board():
    """
    Creates the board at the start of a new round
    """
    board.append(LETTERS)
    for i in range(0, 5):
        board.append([f"{i + 1}"] + ["O"] * 5)


def print_board(board):
    for i in board:
        print(" ".join(i))


def random_int(board):
    return randint(1, len(board)-1)


def random_point():
    """
    Generates 2 random numbers, concatenates them,
    then converts the new number back to an integer for calculation
    """
    point = int(str(random_int(board)) + str(random_int(board)))
    return point


def add_to_list():
    """
    Generates new points and adds them to the coordinates list with no duplicates
    """
    r = random_point()
    if (r in coordinates):
        add_to_list()
    else:
        coordinates.append(r)


def hide_ships():
    """
    Allows the player to choose how many battleships they want to find
    Ensures valid input
    """
    while True:
        amount = input("How many ships would you like hidden? \n")
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
    """
    Gets the desired coordinate from the player,
    coverts it into a 2 digit integer for calculation
    and a point for representation on the visual board
    """
    guess = str(input("Guess coordinates (in the form A1): \n"))

    # Checks that the players guess is legal
    check_length(guess)
    check_col(guess)
    check_row(guess)

    # Conversion for calculation
    number = str(LETTERS.index(guess[0].capitalize())) + guess[1]
    number = int(number)

    check_used(number)

    # Conversion for display
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
    """
    Takes the first character of the player's guess and compares it to the LETTERS list
    """
    col = guess[0].capitalize()
    if (col in LETTERS):
        try:
            x = LETTERS.index(col)
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


def check_used(number):
    if (number in used):
        print("You've already shot there!")
        player_guess()
    else:
        pass


def check_win():
    if (coordinates == []):
        print("You sank my battleships!")
        print("Congratulations!")
        replay()


def replay():
    print('If you would like to play again, enter "Y"')
    replay = input()
    if replay.capitalize() == "Y":
        initialise()
        main()
    else:
        sys.exit()


def check_hit(number, shot):
    """
    Checks if a shot hits or not
    """
    if (number in coordinates):
        print("Hit!")
        coordinates.remove(number)
        print(f"{len(coordinates)} ships left.")

        used.append(number)

        board[shot[1]][shot[0]] = "X"

        check_win()
        print_board(board)
        player_guess()
    else:
        print("Miss!")
        print(f"{len(coordinates)} ships left.")

        used.append(number)

        board[shot[1]][shot[0]] = "0"

        print_board(board)
        player_guess()


def main():
    create_board()
    print_board(board)
    hide_ships()
    print(coordinates)
    player_guess()


main()
