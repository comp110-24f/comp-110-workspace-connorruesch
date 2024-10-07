"""CQ05 - Mutating functions."""

__author__: str = "730739368"


def manual_append(list: list[int], appendee: int) -> None:
    """Appends the appendee to the end of the given list."""
    list.append(appendee)


def double(list: list[int]) -> None:
    """Doubles the given list."""
    index: int = 0

    while index < len(list):
        list[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
