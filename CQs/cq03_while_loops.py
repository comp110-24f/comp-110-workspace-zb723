"""Practicing While Loops"""

__author__ = "730700099"


def num_instances(phrase: str, search_char: str) -> int:
    """ "How many times a letter shows up in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):  # make sure there is a definite stop in the future
        if (
            phrase[index] == search_char
        ):  # using index to go through every letter of the phrase
            count += 1  # If the index letter matches the search character then add 1

        index += 1
    return count
