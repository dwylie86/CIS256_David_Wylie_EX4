# David Wylie
# CIS256 Fall 2025
# EX 4.2 (Unit Tests for Guess The Word)

from guess_the_word import validate_guess, check_win_con, generate_random_word


def test_validate_guess():
    """
    Tests if a single alpha character or not is reconized.
    """
    assert validate_guess("d")
    assert not validate_guess("cat")
    assert not validate_guess(" ")
    assert not validate_guess("")
    assert not validate_guess("4")
    assert not validate_guess("!")


def test_check_win_con():
    """
    Tests if a win condition is recognized.
    """
    assert check_win_con("cake")
    assert not check_win_con("_ake")
    assert not check_win_con("__ke")
    assert not check_win_con("___e")
    assert not check_win_con("____")


def test_generate_random_word():
    """
    Tests if randomly generated word is actually in the referenced word_list.
    """
    test_word_list = [
        "apple", "banana", "orange", "grape", "melon",
        "peach", "cherry", "mango", "lemon", "plum",
        "tiger", "eagle", "dolphin", "rabbit", "falcon",
        "spider", "turtle", "shark", "penguin", "giraffe"
    ]

    assert generate_random_word(test_word_list) in test_word_list
