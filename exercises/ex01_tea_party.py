"""A program to calculate the needs for a tea party."""

__author__: str = "730739368"


def main_planner(guests: int) -> None:
    """Plans the tea party based on the number of guests given."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for X people."""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed, assuming for every tea someone drinks,
    they'll want 1.5 treats."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost based on the number of teas and treats given."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
