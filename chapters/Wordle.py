import random
import sys
def wordle():
    with open('shared/words.txt') as fin:
        words = [line.strip().lower() for line in fin if len(line.strip()) == 5]
    wordle = random.choice(words)
    print("Welcome to Wordle!")
    input_1 = input("Would you like to start (s), learn the rules (r), or exit (e)? ").lower()
    if input_1 not in ["s", "r", "e"]:
        print("Please enter a valid letter, s, r, or e: ")
    elif input_1 == "r":
        print('Enter a 5 letter word. It will tell you if your letters are correct or not. "green" means that the letter is correct and in the right spot, "yellow" means that the letter is correct but not in the right spot, and "gray" means the it is not correct at all. You have 6 attempts. Good luck!')
    elif input_1 == "e":
        print("Thanks for playing!")
        sys.exit() 
    for attempt in range(1, 7):
        guess = input(f"Guess {attempt}/6: ").lower()
        if len(guess) != 5:
            print("Your guess must be 5 letters.")
            continue
        result = [""] * 5
        leftover = list(wordle)
        for i in range(5):
            if guess[i] == wordle[i]:
                result[i] = "green"
                leftover[i] = None

        for i in range(5):
            if result[i] == "":
                if guess[i] in leftover:
                    result[i] = "yellow"
                    leftover[leftover.index(guess[i])] = None
                else:
                    result[i] = "gray"

        print("Result:", result)

        if guess == wordle:
            print(f"You got it! The word was '{wordle}'.")
            return

    print(f"Out of guesses! The word was '{wordle}'.")

wordle()