"""Finding different things in lists whith loops"""

__author__ = "730700099"


def all(list_1: list[int], num: int) -> bool:
    num_count: int = 0
    idx: int = 0
    all_found: bool = False  # quto false if not meet conditions
    while idx <= len(list_1) - 1:
        if num == list_1[idx]:
            num_count += 1
        idx += 1
        if num_count == len(list_1):  # if num_count = then returns True
            all_found = True
    return all_found


def max(list_num: list[int]) -> int:
    largest: int = list_num[0]  # starts from num 1
    for elem in list_num:  # go through every elem
        if elem > largest:
            largest = elem  # recode to be elem if bigger
    if len(list_num) == 0:
        raise ValueError("max() arg is an empty List")  # error
    return largest


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    # need len to be = to work or else False
    # run through every index
    # if 1 idx not = then auto false

    if len(list_1) != len(list_2):  # lists not same len auto False
        return False
    idx: int = 0
    while idx < len(list_2):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True


def extend(a: list[int], b: list[int]) -> None:
    for elem in b:
        a.append(elem)  # append for every element in b
