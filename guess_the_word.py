# David Wylie
# CIS256 Fall 2025
# EX 4.1 (Guess The Word)

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


def validate_guess(guess):
    """
    Function to validate that the guess entered is a valid alpha character
    :params: guess - str - letter guess
    :return: true if the condition is met
    """
    return guess.isalpha() and len(guess) == 1


def check_win_con(running_guess):
    """
    Function to check if the running guess has no blanks left,
    signaling win condition.
    :params: running_guess - str - the current cumulative guess
    :return: true if the condition is met
    """
    return "_" not in running_guess


def generate_random_word(word_list):
    """
    Function to select a random word from a word list
    :params: word_list - list - a list of words to guess
    :return: a random word from the list
    """
    return random.choice(word_list).lower()


def main():
    """
    Main Entry Point of Program:
    Select a random word from a predefined list.
    Prompt the user to guess one letter at a time.
    Reveal letters if the guess is correct; indicate if incorrect.
    Continue until the user guesses the word or runs out of attempts.
    Display a congratulatory message when the word is guessed.
    """
    secret_word = generate_random_word(word_list)
    print(secret_word)
    max_guesses = 10
    guessed_letters = []

    print("-" * 40)
    print("Welcome to the word guessing game!")
    print(f"You have {max_guesses} guesses to guess the word.")
    print(f"Your word has {len(secret_word)} letters in it:")
    print("-" * 40)

    while max_guesses > 0:
        # running_guess builds the current word with correct guesses
        running_guess = ""
        for letter in secret_word:
            if letter in guessed_letters:
                running_guess += letter
            else:
                running_guess += "_"
        if check_win_con(running_guess):
            print(f"The secret word was {secret_word}.")
            print("CONGRATULATIONS! YOU WIN!!!")
            break
        print(f"Secret Word: {running_guess}")
        print(
            f"Guessed Letters: {', '.join(sorted(guessed_letters))}"
            )
        print(f"Guesses Left: {max_guesses}")

        guess = input("Enter a letter: ").lower()
        if validate_guess(guess):
            if guess in guessed_letters:
                print("Letter already guessed, choose again.")
                print("-" * 40)
                continue
            else:
                guessed_letters.append(guess)
                if guess in secret_word:
                    print("Letter Found!")
                    print("-" * 40)
                else:
                    max_guesses -= 1
                    print("Letter NOT Found...")
                    print("-" * 40)

            if max_guesses == 0:
                print(f"The secret word was {secret_word}.")
                print("GAME OVER! Please try again.")
        else:
            print("Please enter a single letter.")
            print("-" * 40)
            continue


# Need this in order to run the testing suite without running the main program
if __name__ == "__main__":
    main()
