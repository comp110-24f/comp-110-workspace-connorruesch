"""Basic syntax of lists."""

my_numbers: list[float] = []  # list literal
# my_numbers: list[float] = list() # list constructor

# String Analoogy
# my_name: str = "" # literal
# my_name: str = str() # constructor

# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)

# Initalizing a list with values already in it
game_points: list[int] = [102, 86, 94]

# Subscription Notation/Indexing
last_game: int = game_points[2]
# print(last_game)

# Modifying by Index
game_points[1] = 72
# print(game_points)

# Getting the Length
# print(len(game_points))

# Remove an item
# game_points.pop(1)
# print(game_points)

# Function name: display
# Parameter: list[int]
# Return value: None
# Print every element in the input list


def display(input_list: list[int]) -> None:
    """Displays all of the elements in input_list."""

    index: int = 0

    while index < len(input_list):
        print(input_list[index])
        index += 1


def display_for(items: list[int]) -> None:
    for x in items:
        print(x)


display(game_points)

game_points.append(102)

print(game_points)


def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1

    print(my_list)


msg: list[int] = [4, 5, 6]
lessen(msg)
