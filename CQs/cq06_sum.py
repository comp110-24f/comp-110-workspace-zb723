"""Summing the elements of a list using different loops"""

__author__ = "730700099"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx += 1
    print(sum)
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0
    for elem in vals:  # no increment needed, run through by self
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0  # base
    for i in range(0, len(vals)):  # range = places to go through
        elem: float = vals[i]  # actually have elem instead of i
        sum += elem  # i b/c i represents the actual num
    return sum
