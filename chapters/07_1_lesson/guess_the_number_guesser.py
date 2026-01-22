# Number Guessing Game - Guesser
# The user thinks of a number between 1 and 100 and the program tries to guess it.
# The user should tell the program if the guess is too high, too low, or correct.
# The program should tell the user how many guesses it took to guess the number.

import random


def get_number_feedback():
    # TODO: Implement this function
    pass


def get_number():
    # TODO: Implement this function
    pass


def play_guesser():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    print('-' * 60)
    print()
    print(f"Think of a number between {MIN_NUMBER} and {MAX_NUMBER} (inclusive).")
    input("Press Enter when you have thought of a number.")
    print()
    guess_count = 0
    # TODO: Implement the rest of this function
    pass

def main():
    print('-' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_guesser()
        answer = input("Do you want to play again? (y/n) ").lower()
        if answer == "n":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()