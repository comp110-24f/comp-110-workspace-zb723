# Lists

# Declaring the type of a list
# <list name>: list[<item name (objects of that list)>]

names: list[str]

# Initializing an empty list
# With a constructor
# list name: list[item type] = list()

# With a literal
# list name: list[item type] = []

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# Adding an item to a list
# <list name>.append(<item>)
# grocery_list.append("bananas") #like caling append(grocery_list, "bananas")
# print(my_numbers)

my_numbers.append(1.5)

# print(my_numbers)

# Add one thing at a time using append

# Initializing an already populated list
# <list nameL: list[<item type>] = [item 0, item 1,...]

game_points: list[int] = [102, 86, 94]
# print(game_points)

# indexing/Subscription notation
# grocery_list: list[str] = ["bananas", "milk", "bread"]
# grocery_list[0]

# print(game_points[2])
last_game: int = game_points[2]  # can save it as a variable
# print(last_game)

# Modifying by Index (bc lists are mutable)
# grocery_list: list[str] = ["bananas", "milk", "bread"]
# grocery_list[1]= "eggs"

game_points[1] = 72
# print(game_points)

# Length of a list
print(len(game_points))

# Remove items from a list
# grocery_list.pop(2)

(game_points.pop(1))
print(game_points)

# Write a fucntion called dispaly
# Input = a list of ints list[int]
# Return value = none
# Loop over input and print every value
# Try calling it on game_points


def display(inp: list[int]) -> None:
    index: int = 0
    while index < len(inp):
        print(inp[index])
        index += 1


(display(game_points))
