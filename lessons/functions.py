"""Practice with functions."""

# from random import randint

# print(randint(10, 50))


# Function Definition
def sum(num1: int, num2: int) -> int:
    """Calculate the sum of num1 and num2, then return it."""
    return num1 + num2


# Syntax note -- parameters are going to be within the function
# signature, arguments are within the function call.

# Function Call
print(sum(num1=2, num2=3))  # <- arguments
