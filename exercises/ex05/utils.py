"""EX05 -- More list utils, tested with unit tests."""

__author__: str = "730736398"


def only_evens(input: list[int]) -> list[int]:
    """Returns a new list of even numbers contained in the given input list."""
    return_list: list[int] = []

    # Loop thorugh all of the integers in input
    for value in input:
        # mod 2 returns 0 if the number is even
        if (value % 2) == 0:
            return_list.append(value)  # add to our new list

    return return_list


def sub(input: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a new list which contains the elements between the given start
    index and the end index - 1."""
    return_list: list[int] = []

    # If the given start index is negative, we just set it to 0.
    if start_index < 0:
        start_index = 0

    # If the end index is greater than the length of the given input list, we
    # just loop through the whole list. Otherwise, we set the end index equal to
    # itself - 1
    if end_index > len(input):
        end_index = len(input) - 1
    else:
        end_index -= 1

    i: int = start_index

    # Use a while loop with i until we reach the end index.
    while i <= end_index:
        return_list.append(input[i])
        i += 1

    return return_list


def add_at_index(input: list[int], value: int, index: int) -> None:
    """Adds the given value to the specific index in given input list."""
    # Index is not in range of what is possible to add to the input list
    # Note: we use len(input) since indices start at 0, and it is possible
    # to extend the list by one within this function
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")

    # If the index is the same as the return value of python's len() function,
    # which is 1 + the last possible index, we just append the given value to
    # the end of the list.
    if index == len(input):
        input.append(value)
        return

    # Add a duplicate of the last item in the list to extend it by one, as
    # we'll be shifting everything over.
    input.append(input[len(input) - 1])

    loop_index: int = len(input) - 2  # -2 to account for the duplicate we just made

    # We shift everything over by working in reverse order, so long as
    # our loop index is greater than the given index, we'll need to move something
    # over to make room.
    while loop_index > index:
        input[loop_index] = input[loop_index - 1]
        loop_index -= 1

    # We've moved everything over, so we can set the given index to the desired value.
    input[index] = value
