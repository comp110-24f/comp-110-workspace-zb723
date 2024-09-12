# Boolean Operators and Conditionals

# Boolean
# Something that evaluates to true or false (relational operators + boolean operators)
# Boolean operators: not, and, or

# Not operator
# inverts the value of a boolean expression

# And operator
# Booleans combined with and evaluate to True if and ONLY if both booleans are True

# or operator
# booleans combined with or evaluate to True if at least one of them is True

# Ordering (what will evaluate first)
# P E MD AS not and or

# Conditionals
# if current card < low card make it the low card
# Conditional Staatements
# if <something>: (something that evaluates to True or False, should be boolean
#    expression)
#    <do something> -> "then" block (what you want it to do if True)
# <rest of program>


def less_than_10(num: int) -> bool:
    """Tell us if num < 10"""
    if num < 10:  # check if this is true
        return True  # "then" block
    else:
        return False


print(less_than_10(num=11))


def less_than_5(num: int) -> int:
    """Tell us if num < 10"""
    if num < 10:  # check if this is true
        return "small number"  # "then" block
    else:
        return "Big number"


print("This is the end of the function")

less_than_10(num=5)


def check_first_letter(word: str, letter: str) -> str:
    """checking 1st letter"""
    if letter == word[0]:
        return "Match!"
    else:
        return "No match!"


print(check_first_letter(word="happy", letter="d"))
