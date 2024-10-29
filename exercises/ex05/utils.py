"""Implementing list utility functions"""

__author__ = "730700099"


def only_evens(list_1: list[int]):
    new_list: list[int] = []  # new empty list for evens
    for elem in list_1:
        if elem % 2 == 0:  # = 0 means even
            new_list.append(elem)  # add every elem to new list
    return new_list


def sub(list_1: list[int], start_idx: int, end_idx: int):
    idx: int = 0
    new_list: list[int] = []
    while idx < len(list_1):
        if start_idx < 0:  # just basic code for procedures wanted in instructions
            start_idx = 0
        if end_idx > len(list_1):
            end_idx = len(list_1) + 1
        if (
            len(list_1) == 0 or start_idx >= len(list_1) or end_idx == 0
        ):  # return empty list
            return new_list
        if (
            idx >= start_idx and idx < end_idx
        ):  # only care if idx is btwn 2 numbers, then adds to new_list
            new_list.append(list_1[idx])
        idx += 1
    return new_list


def add_at_index(list1: list[int], elem: int, chosen_idx: int) -> None:
    # Plan:
    #   Add extra elem (make space for new one)
    #   Shift elems after chosen_idx to right (make space)
    #       have to start from end (right -> left)
    #       make idx len(list) - 1
    #   Recode from right to left to avoid repeat nums
    #   Recode prev elem @ chosen_idx to new one
    if chosen_idx < 0 or chosen_idx > len(list1):  # raise errors
        raise IndexError("Index is out of bounds for the input list")
    list1.append(
        0
    )  # add to list before start while loop so can add to empty lists if possible
    idx: int = len(list1) - 1  # To start at end of list
    if idx < len(list1):
        while idx >= chosen_idx:  # stop at chosen idx, only shift those after chosen
            if idx > chosen_idx:
                list1[idx] = list1[idx - 1]  # move right to left
            if idx == chosen_idx:  # if equal, stop and replace
                list1[idx] = elem
            idx -= 1  # keep loop going
    return None
