"""An example of recursive functions."""


def factorial(n: int) -> int:
    """Compute the factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))