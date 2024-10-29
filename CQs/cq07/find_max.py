"""finding the max in a list then removing it"""

__author__ = "730700099"


def find_and_remove_max(input: list[int]) -> int:
    """finding the biggest number, removing it from the list, but return max num"""
    # have largest be a variable to compare while going through list
    # Also saves largest so it can return
    # Need something to keep track of where max idx is
    # While loop so easy to see what doing + keep track
    # if elem > largest then it becomes new largest
    # hard code when list = 0
    # remove largest num (save the index)
    # have to remove largest @ every idx/occurence
    idx: int = 0
    max_idx: int = 0
    if len(input) == 0:
        return -1
    max: int = input[0]
    if len(input) > 0:
        while idx < len(input):
            if input[idx] > max:  # to do if greater
                max = input[idx]
                max_idx = idx
            if input[idx] == max and idx != max_idx:
                input.pop(idx)  # pop it if equal but a diff index
            idx += 1  # keep loop going
        input.pop(max_idx)  # pop idx w/ max, after finding through loop
    return max
