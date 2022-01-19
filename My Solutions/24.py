print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    """Return the square value of the input number.

    The input number must be integer.
    """
    return num ** 2


n = float(input())
print(square(n))
print(square.__doc__)
