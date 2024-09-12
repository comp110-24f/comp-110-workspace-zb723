"""Practice with functions"""

from random import randint

print(randint(1, 10))

print("hello")
"""Parameter is generic (integer) vs argument (2)
    Return type: generic what you want your result to be"""


# Define a function
def sum(num1: int, num2: int) -> int:
    """Returns sum of 2 numbers (num1 and num2)."""
    return num1 + num2


# Call the function
print(sum(num1=1, num2=10))  # <- 1 and 10 are arguments
