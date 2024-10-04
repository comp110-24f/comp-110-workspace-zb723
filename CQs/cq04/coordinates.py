"""idk what this does yet"""

__author__ = "730700099"


def get_coords(xs: str, ys: str) -> None:
    index_x: int = 0  # index 4 x coord
    index_y: int = 0  # index 4 y coord
    while index_x < len(xs):
        index_y: int = 0  # resets so x coord gets every y coord
        while index_y < len(ys):
            print("(" + xs[index_x] + "," + ys[index_y] + ")")
            index_y += 1
        index_x += 1


get_coords("123", "abc")
