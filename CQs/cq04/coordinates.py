"""CQ04 - A function for printing formatted pairs."""

__author__: str = "730739368"


def get_cords(xs: str, ys: str) -> None:
    """Prints the formatted pairs of each character in the two input strings."""
    index1: int = 0
    index2: int = 0

    while index1 < len(xs):
        # Use a nested while loop to iterate over the second input
        while index2 < len(ys):
            print(f"({xs[index1]}, {ys[index2]})")
            index2 += 1

        index1 += 1  # Increase the index for our first character
        index2 = 0  # Reset the second index, in the event that we need to iterate again


if __name__ == "__main__":
    get_cords("hi", "bye")
