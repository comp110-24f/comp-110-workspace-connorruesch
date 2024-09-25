"""A recreation of the popular New York Times game, Wordle."""

__author__: str = "730739368"


def input_guess(secret_word_length: int) -> str:
    """Checks to make sure the guess word is the same length as the
    secret word--if it is, we return the guess word."""

    guess_word: str = input(f"Enter a {secret_word_length} character word: ")

    # Had to be a little more creative with this, since we have two potential cases
    # that we're trying to prevent: if the number of the characters in the guess word
    # is less than the length of the secret word, and if it is higher. My solution: if
    # it isn't, we just continually prompt the user for an input, and keep changing the
    # guess word variable until they enter a word of the correct length.
    while len(guess_word) != secret_word_length:
        # Since python's input() function halts the program execution until a user
        # enters an input, all we have to do is change our guess_word variable
        # and continually evaluate what the length of it is.
        guess_word = input(f"That wasn't {secret_word_length} chars! Try again: ")

    return guess_word


def contains_char(searched_string: str, character: str) -> bool:
    """A function that returns true if the given character is present in
    the searched string, and false is otherwise not."""
    assert len(character) == 1

    index: int = 0

    while index < len(searched_string):
        if searched_string[index] == character:
            return True
        else:
            index += 1

    # Will only return false if the while loop above doesn't find
    # any instances where the given character is present in the
    # searched word. Remember: we only need to find the first occurnace
    # of the given character in the word, once we do, we can return.
    return False
