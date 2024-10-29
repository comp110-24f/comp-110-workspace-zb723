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


# For In loops in memore

my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for elem in my_list:  # actually creating variable elem and gets first value in my_list
    new_list.append(elem)
print(new_list)

# For loop syntax practice
pets: list[str] = ["Lpuis", "Bp", "Bear"]
for animal in pets:
    print(f"Good boy {animal}!")

# Why while loop over for loop
#   special condition NOT related to a sequence 
#   Looping over and modifying it wile your doing it 

names: list[str]: ["Al", "Janet","Viranda"]
for index in range(0, len(names)): #list the range for where tou want to search/loop
    print(str(index) + ":" + names[index])