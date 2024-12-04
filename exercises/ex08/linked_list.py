"""EX08 - Linked List Utils."""

from __future__ import annotations

__author__: str = "730736398"


class Node:
    """A basic node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Create a new node instance w/ a value and the next node (or none)."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str  # create our rest string that we will initalize later
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)

        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the node at the given index in the linked list."""
    # Base case: index is 0, return the value of the current node
    # Recursive case: index > 0, we call the function again w/ the index being index - 1
    # Err: if the index is 0, and head is none, then we need to raise an error.
    if head is None:
        # If the function is being called and head is None, then that means the list is
        # either empty, or our index is out of bounds--so we raise an Index error.
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:
        # Index is 0, which is our base case, so we return the value of head.
        return head.value
    else:
        # Our recursive case--we need to get closer to our base case to get down
        # to the value at our specific index.
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")

    # Base case: we are on the last element in the list
    # Recursive case: there is another element in the list that we need to compare to
    if head.next is None:
        return head.value
    else:
        # Calculate the maximum value of any further nodes in the linked list
        next: int = max(head.next)

        # Compare the current head's value with the current maximum value so far
        if head.value > next:
            return head.value  # the head's value is bigger, so we return that
        else:
            return next  # the head's value is smaller, so our maximum remains the same


def linkify(items: list[int]) -> Node | None:
    """Creates a linked list based on the given list of integers."""
    # Base case: list of items is empty
    # recursive case, we need to add more items
    if len(items) == 0:
        return None
    else:
        # Create a new node with the first element in the list, then
        # calculate the next by doing the same with the element after it,
        # and continue until there aren't any more elements in the list
        # anymore.
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list with node values multiplied by the given factor."""
    # Base case: the given head is none, so we return none
    # Recursive case: head is not none, to which we need to multiply it's value and
    # calculate the other nodes in the linked list as well
    if head is None:
        return None
    else:
        # Multiply the current node's value and calculate the next node as well
        return Node(head.value * factor, scale(head.next, factor))
