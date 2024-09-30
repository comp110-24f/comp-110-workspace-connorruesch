"""CQ04 - A string concatenation function."""

__author__: str = "730739368"

word1: str = "happy"
word2: str = "tuesday"


def concat(string1: str, string2: str) -> str:
    """Concatenates the two given strings into a single string."""
    return f"{string1}{string2}"


# only run if we are explicity running this module
if __name__ == "__main__":
    print(concat(word1, word2))
