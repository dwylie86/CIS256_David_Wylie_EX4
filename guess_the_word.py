# David Wylie
# CIS256 Fall 2025
# EX 4.1 (Guess The Word)

# Implement the game with the following features:
# Select a random word from a predefined list.
# Prompt the user to guess one letter at a time.
# Reveal letters if the guess is correct; indicate if incorrect.
# Continue until the user guesses the word or runs out of attempts.
# Display a congratulatory message when the word is guessed.
    # "code",
    # "deafault",
    # "topaz",
    # "memory",
    # "quiz",
    # "karate",
    # "computer",
    # "snake",
    # "python",
    # "language"
    # random.randint(0, len(WORD_LIST))

import random

WORD_LIST = [
    "cake"
]

secret_word = WORD_LIST[0]
print(secret_word)
MAX_GUESSES = 10

print("Welcome to the game!")
print(f"You have {MAX_GUESSES} Guesses")
print(f"Your Word has {len(secret_word)} letters in it:")
for i in secret_word:
    print("_", end=" ")
print()

guess = input("Enter a letter: ")
MAX_GUESSES -= 1
if guess in secret_word:
    print("Letter Found!")
else:
    print("Letter NOT Found...")

for index, letter in enumerate(secret_word):
    if letter != guess:
        print("_", end=" ")
        
    else:
        print(letter, end=" ")
        
print(f"\nYou have {MAX_GUESSES} guesses left")
