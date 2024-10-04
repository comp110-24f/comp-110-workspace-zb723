"""Mutating functions"""

__author__ = "730700099"


def manual_append(a: list[int], num: int) -> None:
    a.append(num)  # adding to the list


def double(b: list[int]) -> None:  # run each number and * by 2
    idx: int = 0
    while idx < len(b):  # to go through each num but has a def stop
        b[idx] = b[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # equal to list 1, ref the same list

double(list_2)  # i think both are going to print the same thing
print(list_1)  # What happened: they print the same bc they both ref
print(list_2)  # the same list, so their results change tgt
