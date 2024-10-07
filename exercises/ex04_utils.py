"""EX04 - A set of list utility functions to understand algorithmic constructs."""

__author__: str = "730739368"


def all(input: list[int], value: int) -> bool:
    """Returns true if all the elements in the provided list match the given int."""

    index: int = 0

    # We first check to make sure that the list isn't empty, if it is,
    # we go ahead and return false.
    if len(input) == 0:
        return False

    # Search to check if there any integers in the list that do NOT match
    # the value that we are given. My philosophy is this: since we are trying
    # to prove that all elements in the given list match the individual value
    # we're looking at, it is easier to find one counterexample to return false,
    # and if we don't find anything-- we can go ahead and return true.
    while index < len(input):
        if input[index] != value:
            return False
        index += 1

    return True


def max(input: list[int]) -> int:
    """Returns the largest int in the given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # List cannot be empty.

    index: int = 0
    largest_num: int = 0

    # We note down the largest number we have come across so far, and
    # if there is another element in the list that is larger than that--
    # we go ahead and note that down instead. By the end of the loop,
    # we'll be able to know which is the largest number and return it.
    while index < len(input):
        if input[index] > largest_num:
            largest_num = input[index]

    return largest_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if the two given lists contain the same elements at the same indexes."""
    # The the two lists are of different lengths, we automatically know that
    # they do not contain the same exact elements at every index.
    if len(list_1) != len(list_2):
        return False

    index: int = 0

    # Similiar methodology to what is described above: we just need to look for
    # one case where the elements at each index don't match to disprove that
    # they contain the same elements, and if we can't prove that, that means
    # we have two lists that do contain the same elements.
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            return False
        index += 1

    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Adds the elements of list_2 to list_1."""
    index: int = 0

    # Loop through list_2 and append all of it's elements to list_1.
    while index < len(list_2):
        list_1.append(list_2[index])
        index += 1
