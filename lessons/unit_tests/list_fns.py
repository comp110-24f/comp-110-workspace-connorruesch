"""A series of list functions."""


def get_first(input: list[str]) -> str:
    """Returns the first element of the given list."""
    if len(input) == 0:
        return ""

    return input[0]


def remove_first(input: list[str]) -> None:
    """Removes the first element of the given list."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Removes and returns the first element of the given list."""
    return input.pop(0)
