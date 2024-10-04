"""idk what this does yet"""

__author__ = "730700099"

from CQs.cq04.concatenation import concat  # importing function

from CQs.cq04.coordinates import get_coords

x: str = "123"  # global variables
y: str = "abc"

print(concat(x, y))

print(get_coords(x, y))
