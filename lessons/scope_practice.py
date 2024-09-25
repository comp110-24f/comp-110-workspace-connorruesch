"""Scope examples!"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if not (msg[index] == char):
            copy += msg[index]
        index += 1
    return copy


# word: str = "yoyo"  # global variable
# print(remove_chars(msg=word, char="y"))
