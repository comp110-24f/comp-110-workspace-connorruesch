"""CQ03 -- While Loops"""

__author__: str = "730739368"


def num_instances(phrase: str, search_char: str) -> None:
    """Checks the number of occurances of a specific letter in the given phrase."""
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1

        index += 1

    print(str(count))


num_instances(phrase="Happy Tuesday!", search_char="z")
