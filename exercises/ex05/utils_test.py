from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""EX05 -- More list utils, tested with unit tests."""

__author__: str = "730736398"


def test_only_evens_return_value() -> None:
    """only_evens should return a new list with only even numbers."""
    assert only_evens(input=[4, 5, 6, 7, 8]) == [4, 6, 8]


def test_only_evens_mutation() -> None:
    """only_evens should not mutate the given input list."""
    integer_list: list[int] = [4, 5, 6, 7, 8]
    only_evens(input=integer_list)
    # We don't need to pay attention to the return value of only_evens,
    # only that integer_list stays the same after we pass it through the
    # function.
    assert integer_list == [4, 5, 6, 7, 8]


def test_only_evens_edge_case() -> None:
    """only_evens should work with negative values."""
    assert only_evens(input=[-4, -5, 6, 7, 8]) == [-4, 6, 8]
    # I've included -5 as well to show that it works with odd numbers
    # being negative as well.


def test_sub_return_value() -> None:
    """sub should return a new list that contains elements from the input list
    between the given start index and end index - 1"""
    assert sub(input=[3, 4, 5, 6], start_index=1, end_index=3) == [4, 5]


def test_sub_mutation() -> None:
    """sub should not mutate the given input list"""
    integer_list: list[int] = [3, 4, 5]
    sub(input=integer_list, start_index=1, end_index=2)
    # Again, we aren't concerned with the return value of sub here,
    # only that integer_list remains the same.
    assert integer_list == [3, 4, 5]


def test_sub_edge_case() -> None:
    """sub should work when the beginning or end indices are out of bounds, if
    both are out of bounds it should just return the same values as the given
    input list."""
    assert sub(input=[3, 4, 5], start_index=-1, end_index=4) == [3, 4, 5]


def test_add_at_index_return_value() -> None:
    """add_at_index should return None"""
    assert add_at_index(input=[2, 3, 4, 5], value=0, index=2) is None


def test_add_at_index_mutation() -> None:
    """add_at_index should mutate the given input list"""
    integer_list: list[int] = [2, 3, 4, 5]
    add_at_index(input=integer_list, value=0, index=2)
    assert integer_list == [2, 3, 0, 4, 5]


def test_add_at_index_edge_case() -> None:
    """add_at_index should raise IndexError if the index is out of bounds"""
    with pytest.raises(IndexError):
        add_at_index(input=[2, 3, 4, 5], value=0, index=10)
