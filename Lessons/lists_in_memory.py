# Lists in Memory: Comparing Lists and Strings
# strings are just stored in the stack, lists are stored in the heap
# Variables that are lsists are just a reference to the list
#   (pointing to the list location)

# Lists + functions
#   functions can
#       Take lists as arguments
#       Return or create lists
#       Modify lists


def display(vals: list[int]) -> None:
    idx: int = 0
    while idx < len(vals):
        print(vals[idx])
        idx += 1
