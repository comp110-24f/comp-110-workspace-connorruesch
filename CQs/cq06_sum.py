"""Summing the elements of a list using different loops"""

__author__: str = "730739368"


def w_sum(vals: list[float]) -> float:
    """Returns the su of all values in the given list. Uses a while loop."""
    count: float = 0.0  # Create our counter variable
    index: int = 0

    while index < len(vals):
        count += vals[index]
        index += 1

    return count


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all values in the given list. Uses a for loop."""
    count: float = 0.0

    for x in vals:
        count += x

    return count


def f_range_sum(vals: list[float]) -> float:
    """Returns the sun of all values in the given list. Uses the range function."""
    count: float = 0.0

    for index in range(0, len(vals)):
        count += vals[index]

    return count
