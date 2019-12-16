def factorial(i: int) -> int:
    """
    i : int
    """
    if i < 0:
        return None
    if i == 0:
        return 1
    return i * factorial(i - 1)

print(factorial(9.0))
import sys
print(sys.version)




