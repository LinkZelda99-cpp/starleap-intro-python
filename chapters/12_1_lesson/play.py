import random
from typing import Optional

MIN_NUMBER: int = 1
MAX_NUMBER: int = 100


def get_guess() -> int:
    """Prompt the user until they enter a valid integer in range.

    Returns the validated integer.
    """
    # Prompt text shown to the user for each guess.
    # Kept as a variable so it can be easily changed or localized.
    prompt = "Enter your guess: "

    while True:
        raw = input(prompt)
        # Convert input to integer, handling invalid input gracefully.
        # If conversion fails, inform the user and repeat the loop.
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Ensure the guess falls within the allowed range.
        # If it doesn't, show a helpful message and prompt again.
        if not (MIN_NUMBER <= guess <= MAX_NUMBER):
            print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
            continue

        return guess


def evaluate_guess(guess: int, target: int) -> Optional[str]:
    """Return feedback string when guess is incorrect, otherwise None.

    Feedback messages are preserved to maintain existing behavior.
    """
    # Compare the guess to the target and return a feedback message
    # when the guess is incorrect. Returning None signals a correct guess.
    if guess < target:
        return "Too low! Try again."
    if guess > target:
        return "Too high! Try again."
    return None


def play_guess_number() -> None:
    """Run the guess-the-number game loop."""
    # Choose a random target number for this session and initialize
    # the attempt counter.
    target = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    # Welcome message explaining the rules to the player.
    print(
        f"Welcome to the guess the number game! I'm thinking of a number between "
        f"{MIN_NUMBER} and {MAX_NUMBER}."
    )

    while True:
        # Get a validated guess from the user and increment the attempt count.
        guess = get_guess()
        attempts += 1

        # Check the guess and either provide feedback or end the game.
        feedback = evaluate_guess(guess, target)

        if feedback:
            # Incorrect guess; show hint and loop for another attempt.
            print(feedback)
            continue

        # Correct guess; congratulate the player and display attempts.
        print(f"Congratulations! You've guessed the number {target} in {attempts} attempts!")
        break


def main() -> None:
    play_guess_number()


if __name__ == "__main__":
    main()

            