"""My first exersize in COMP110!"""

__author__ = "730700099"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello," + name + "!"


print(greet("zyah"))


def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1


msg: list[int] = [4, 5, 6]
print(lessen(msg))
