# David Wylie
# CIS256 Fall 2025
# EX 4.1 (Guess The Word)

# Implement the game with the following features:
# Select a random word from a predefined list.
# Prompt the user to guess one letter at a time.
# Reveal letters if the guess is correct; indicate if incorrect.
# Continue until the user guesses the word or runs out of attempts.
# Display a congratulatory message when the word is guessed.


import random

word_list = [
    "cake",
    "code",
    "default",
    "topaz",
    "memory",
    "quiz",
    "karate",
    "computer",
    "snake",
    "python",
    "language"
]

secret_word = random.choice(word_list).lower()
print(secret_word)
max_guesses = 10
guessed_letters = []

print("Welcome to the word guessing game!")
print(f"You have {max_guesses} guesses to guess the word.")
print(f"Your word has {len(secret_word)} letters in it:")
print()

while max_guesses > 0:
    running_guess = ""
    for letter in secret_word:
        if letter in guessed_letters:
            running_guess += letter
        else:
            running_guess += "_"
    print(f"Secret Word: {running_guess}")
    print(
        f"Guessed Letters: {', '.join(sorted(guessed_letters))}"
        )
    print(f"Guesses left: {max_guesses}")

    if "_" not in running_guess:
        print("CONGRATULATIONS! YOU WIN!!!")
        break

    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    elif guess in guessed_letters:
        print("Letter already guessed.")
        continue
    else:
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Letter Found!")
        else:
            print("Letter NOT Found...")

        max_guesses -= 1
        if max_guesses == 0:
            print("GAME OVER! Please try again.")
            print(f"the secret word was {secret_word}")
        else:
            print(f"\nYou have {max_guesses} guesses left")
