# Number Guessing Game - Picker
# The program thinks of a number between 1 and 100 and the user tries to guess it.
# The program should tell the user if the guess is too high or too low.
# The program should also tell the user how many guesses it took to guess the number.
import random

MIN_NUMBER = 1
MAX_NUMBER = 100

print("Think of a number between 1 and 100. Press Enter when you're ready.")
input()
guess_count = 0
while True:
    guess_count += 1
    guess = (MIN_NUMBER + MAX_NUMBER) // 2
    print(f"My guess is: {guess}")
    response = input("Is my guess too high (h), too low (l), or correct (c)? ").lower()
    if response == "c":
        print(f"Yay! I guessed the number in {guess_count} attempts.")
        break
    elif response == "h":
        MAX_NUMBER = guess - 1
    elif response == "l":
        MIN_NUMBER = guess + 1 