"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tll me if num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


# less_than_10(num=5)


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


# print(check_first_letter(word="test", letter="e"))


def get_weather_report() -> str:
    """Display weather instructions."""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


# get_weather_report()


x: int = 1
x = x + 1
print(x)
