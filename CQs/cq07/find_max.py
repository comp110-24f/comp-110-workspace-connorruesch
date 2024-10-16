"""CQ07 - Unit Tests"""

__author__: str = "730736398"


def find_and_remove_max(input: list[int]) -> int:
    """Finds and removes the maximum value from the given list."""
    if len(input) == 0:
        return -1

    index: int = 0
    max_value: int = input[0]

    # Search for the maximum value in the list
    while index < len(input):
        if input[index] > max_value:
            max_value = input[index]
        index += 1

    index = 0  # reset our index variable

    # Remove all instances of that value
    while index < len(input):
        if input[index] == max_value:
            input.pop(index)
        else:
            index += 1

    return max_value
