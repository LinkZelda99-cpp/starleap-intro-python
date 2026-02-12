def guess_number_game():
    import random
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the guess the number game! I'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
                break
        except ValueError:
                print("Please enter a valid integer.")
                
guess_number_game()

            