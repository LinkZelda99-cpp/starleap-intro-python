# Number Guessing Game - Picker
# The program thinks of a number between 1 and 100 and the user tries to guess it.
# The program should tell the user if the guess is too high or too low.
# The program should also tell the user how many guesses it took to guess the number.

MIN_NUMBER = 1
MAX_NUMBER = 100

def get_valid_guess():
    # TODO: Implement this function
    pass

def play_picker():
    # TODO: Implement this function
    pass

def main():
    print('=' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_picker()
        answer = input("Do you want to play again? (y/n) ").lower()
        if answer == "n":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()