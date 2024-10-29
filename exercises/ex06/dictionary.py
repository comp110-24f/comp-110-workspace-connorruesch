"""EX06 -- Utils for dictionaries."""

__author__: str = "730736398"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in the given dictionary and returns a new one. Raises
    KeyError if there are duplicate values in the given dictionary."""
    # An empty dictonary that we will eventually return.
    inverted_dict: dict[str, str] = {}

    for key in input:
        # Get the value of the key in the original dictionary.
        value: str = input[key]

        if value in inverted_dict:
            raise KeyError("Key already exists in return_dict")
        else:
            # Invert the key and value and add to our empty dictionary.
            inverted_dict[value] = key

    return inverted_dict


def favorite_color(input: dict[str, str]) -> str:
    """Tallys the number of favorite colors in the given input dictionary and returns
    the color with the highest tally."""
    # Dictionary for tallying our colors.
    tally_dict: dict[str, int] = {}

    # Tally each person's favorite color by looping through the given dictionary.
    for name in input:
        color: str = input[name]

        if color in tally_dict:
            tally_dict[color] += 1
        else:
            tally_dict[color] = 1

    # Establish variables for what is currently the highest color and the highest
    # tally for that color.
    highest_color_name: str = ""
    highest_color_tally: int = 0

    # Loop through our tally, checking to see which is highest.
    for color in tally_dict:
        tally: int = tally_dict[color]

        if tally > highest_color_tally:
            highest_color_name = color
            highest_color_tally = tally

    # Return the highest tallied color.
    return highest_color_name


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of times a specific value appears in the given input list."""
    # Create our dictionary to tally each value in the list.
    tally_dict: dict[str, int] = {}

    # Loop through the values of our input list.
    for item in input:
        if item in tally_dict:
            # If the value is a duplicate, we increment by 1.
            tally_dict[item] += 1
        else:
            # If the value is not a duplicate, add it to our tally.
            tally_dict[item] = 1

    return tally_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Groups values in the given input list by their first letter and returns a dict
    with those groupings."""
    alphabetized: dict[str, list[str]] = {}

    # Loop through each item in the given input list.
    for item in input:
        # Grab the first letter for readability.
        first_letter: str = item[0]

        if first_letter in alphabetized:
            # Already a value with this first letter, so append the word
            alphabetized[first_letter].append(item)
        else:
            # Add a new key/value pair with the first letter & word
            alphabetized[first_letter] = [item]

    return alphabetized


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates the given attendance log with the day of the week the given student
    attended."""
    if day in attendance_log:
        # Similar logic to the alphabetizer function, if the day of the week is already
        # in the log, then we just append the student to the list of students that
        # attended that day. Additionally, if the student has already been recorded for
        # that day, then we don't need to do anything.
        if not (student in attendance_log[day]):
            attendance_log[day].append(student)
    else:
        # Otherwise, we add the day of the week and the student.
        attendance_log[day] = [student]
