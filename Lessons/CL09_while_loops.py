# Repeat while condition is true
# If true, then we do lines 3 and 4
# Repeatedly until at the end of the "deck"

# Syntax
# While <condition> should be a boolean expression (true or false)
# Repeat actions (wtv you want it to do repeatedly)


def characters(msg: str) -> None:
    index: int = 0
    while index > len(msg):
        print(msg[index])
        index = index + 1


characters(msg="Bedtime")

# There needs to be some future in your code where statement is false
# or else you get an infinite loop

# Relative Reassignment Operators
# Reassigning a variable relative to its current value: i = i +1
# Addition reassignment operator shorthand has the same effect i += 1
