"""A recreation of the popular New York Times game, Wordle."""

__author__: str = "730739368"

# Define the emojis we'll be using in the actual game here.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_length: int) -> str:
    """Checks to make sure the guess word is the same length as the
    secret word--if it is, we return the guess word."""

    guess: str = input(f"Enter a {secret_word_length} character word: ")

    # Had to be a little more creative with this, since we have two potential cases
    # that we're trying to prevent: if the number of the characters in the guess word
    # is less than the length of the secret word, and if it is higher. My solution: if
    # it isn't, we just continually prompt the user for an input, and keep changing the
    # guess word variable until they enter a word of the correct length.
    while len(guess) != secret_word_length:
        # Since python's input() function halts the program execution until a user
        # enters an input, all we have to do is change our guess_word variable
        # and continually evaluate what the length of it is.
        guess = input(f"That wasn't {secret_word_length} chars! Try again: ")

    return guess


def contains_char(searched: str, char: str) -> bool:
    """A function that returns true if the given character is present in
    the searched string, and false is otherwise not."""
    assert len(char) == 1

    index: int = 0

    while index < len(searched):
        if searched[index] == char:
            return True
        else:
            index += 1

    # Will only return false if the while loop above doesn't find
    # any instances where the given character is present in the
    # searched word. Remember: we only need to find the first occurnace
    # of the given character in the word, once we do, we can return.
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns a string of black, yellow, or green emojis depending on whether or
    not the guess matches the secret word. Black indicates a character isn't in
    the word, yellow indicates that it is, it just isn't in the correct position,
    and green indicates that a character is both in the word and in the correct
    position."""
    assert len(guess) == len(secret_word)

    # Define our initial string, we will concatenate to it as we search through
    # the words.
    emojified_string: str = ""

    # Index for searching.
    index: int = 0

    while index < len(guess):
        if guess[index] == secret_word[index]:
            emojified_string += f"{GREEN_BOX}"
        elif contains_char(searched=secret_word, char=guess[index]):
            emojified_string += f"{YELLOW_BOX}"
        else:
            emojified_string += f"{WHITE_BOX}"

        index += 1

    return emojified_string


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""

    # Define which turn we are on.
    turn: int = 1

    # Check to make sure that we haven't used all of our turns
    # already, if we have-- we can exit.
    if turn > 6:
        print("X/6 - Sorry, try again later!")
        exit()

    # Initiate our primary game loop.
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")

        # Gather our user input.
        input: str = input_guess(secret_word_length=len(secret_word))

        # Output emojified string.
        print(emojified(guess=input, secret_word=secret_word))

        # Check to see if the user has won, if they have, then
        # we can go ahead and exit the game loop.
        if input == secret_word:
            print(f"You won in {turn}/6 turns!")
            exit()

        turn += 1


if __name__ == "__main__":
    main(secret_word="codes")
