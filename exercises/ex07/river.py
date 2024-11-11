"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730736398"


class River:
    """A river class for simulating a river."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bear."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks individual ages of bears and fish in the river and removes them."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []

        # If a fish is younger than four, we keep it.
        for fish in self.fish:
            if not (fish.age > 3):
                surviving_fish.append(fish)

        # If a bear is younger than six, we keep it.
        for bear in self.bears:
            if not (bear.age > 5):
                surviving_bears.append(bear)

        # Reassign our bears and fish.
        self.fish = surviving_fish
        self.bears = surviving_bears

    def remove_fish(self, amount: int) -> None:
        """Removes the given amount of fish from the river."""
        i: int = 0
        # Loop through the list of fish in the river and remove it based off the
        # amount specified.
        while i < amount:
            self.fish.pop(i)
            i += 1

    def bears_eating(self) -> None:
        """Simulates bears eating."""
        # If there are more than 5 fish in the river, than each bear may eat three.
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Removes bears with a hunger score less than 0."""
        surviving_bears: list[Bear] = []

        # If a bear isn't starving, then it survives.
        for bear in self.bears:
            if not (bear.hunger_score < 0):
                surviving_bears.append(bear)

        # Reassign our list of bears.
        self.bears = surviving_bears

    def repopulate_fish(self) -> None:
        """Simulates the reproduction of fish in the river."""
        fish_amount: int = len(self.fish)
        # calculate the number of reproduced fish
        reproduce_amount: int = (fish_amount // 2) * 4

        i: int = 0

        # Add the number of reproduced fish
        while i < reproduce_amount:
            self.fish.append(Fish())
            i += 1

    def repopulate_bears(self) -> None:
        """Simulates the reproduction of bears in the river."""
        bears_amount: int = len(self.bears)
        # calculate the number of reproduced bears
        reproduce_amount: int = bears_amount // 2

        i: int = 0

        # add  the number of reproduced bears
        while i < reproduce_amount:
            self.bears.append(Bear())
            i += 1

    def view_river(self) -> None:
        """Prints the fish and bear populations on the current day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week of life in the river."""
        # Simulate seven days in the river.
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
