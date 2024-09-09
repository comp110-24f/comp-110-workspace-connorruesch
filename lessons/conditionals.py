"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tll me if num is < 10."""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


# less_than_10(num=11)


def should_i_eat(hungry: bool) -> None:
    if hungry:  # conditional/boolean expression
        print("eat!")  # "then" block
    else:
        print("don't eat!")  # "else" block
    print("just don't starve!")  # either way


# should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """Checks to see if the first letter of word matches the given letter."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="test", letter="e"))
