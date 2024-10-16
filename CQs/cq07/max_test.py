from CQs.cq07.find_max import find_and_remove_max

"""CQ07 - Unit Tests"""

__author__: str = "730736398"


def test_find_and_remove_max_return_value() -> None:
    """find_and_remove_max should return the maximum value in the list,
    in this case 5"""
    assert find_and_remove_max(input=[1, 2, 3, 5, 4]) == 5


def test_find_and_remove_max_mutate() -> None:
    """find_and_remove_max should remove all instances of the maximum
    value from the list."""
    input: list[int] = [1, 2, 3, 5, 5, 5]
    find_and_remove_max(input=input)
    assert input == [1, 2, 3]


def test_find_and_remove_max_edge_case() -> None:
    """find_and_remove_max should work with an empty list."""
    assert find_and_remove_max(input=[]) == -1
