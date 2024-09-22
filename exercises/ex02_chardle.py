"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730739368"


def main() -> None:
    """Our main function, which handles the entry point for the program."""
    contains_char(word=input_word(), character=input_letter())


def input_word() -> str:
    """Collect a 5-letter input word from the user."""
    word: str = input("Enter a 5-character word: ")

    # Check to make sure the word is 5 characters, if it isn't,
    # exit the program.
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # Invalid input: exit the program.


def input_letter() -> str:
    """Collect an input letter from the user."""
    letter: str = input("Enter a single character: ")

    # Check to make sure teh given input is a single character,
    # if it isn't, inform the user and exit the program.
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, character: str) -> None:
    """Checks to see if there are any chracters within the given
    word, and if there are: prints their indices."""
    print("Searching for " + character + " in " + word)

    count: int = 0

    if word[0] == character:
        print(character + " found at index 0")
        count = count + 1

    # Note we cannot use 'elif' statements here
    # as if there were multiple indices of the given
    # letter, only the last one would be printed. Thus,
    # we need to use multiple, singular 'if' statements.
    if word[1] == character:
        print(character + " found at index 1")
        count = count + 1

    if word[2] == character:
        print(character + " found at index 2")
        count = count + 1

    if word[3] == character:
        print(character + " found at index 3")
        count = count + 1

    if word[4] == character:
        print(character + " found at index 4")
        count = count + 1

    # If there were instances of the letter found in the word, print the amount
    # out, otherwise inform the user that there were none.
    if count != 0:
        print(str(count) + " instances of " + character + " found in " + word)
    else:
        print("No instances of " + character + " found in " + word)


# Run our program!
if __name__ == "__main__":
    main()
