"""File to define Fish class."""

__author__: str = "730736398"


class Fish:
    """A fish class that keeps track of a fish's age."""

    age: int

    def __init__(self):
        """Creates a new fish with the age of zero."""
        self.age = 0

    def one_day(self) -> None:
        """Increases the age by 1 after one day."""
        self.age += 1
