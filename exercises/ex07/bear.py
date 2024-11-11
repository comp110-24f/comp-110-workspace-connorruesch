"""File to define Bear class."""

__author__: str = "730736398"


class Bear:
    """A Bear class that keeps track of it's age and hunger score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Creates a new bear with a age and hunger score of zero."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Increases the age and decreases hunger score by 1 after one day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increases the hunger score by the number of fish the bear ate."""
        self.hunger_score += num_fish
