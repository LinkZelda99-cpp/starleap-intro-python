secret_word = "python"
s = secret_word.split()
guess = ""
correct_guessed_letters = []
for letter in secret_word:
    while guess not in s:
     guess = input("Enter your guess: ")
     if guess == letter in s:
            print("Correct letter!")
            s.append(guess)
     else:
        print("Wrong guess. Try again!")
