"""The first challenge question involving functions."""

__author__ = "730736398"


def mimic(message: str) -> str:
    """Mimics the message given."""
    return message


def main() -> None:
    """The main function designed to execute the program."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
