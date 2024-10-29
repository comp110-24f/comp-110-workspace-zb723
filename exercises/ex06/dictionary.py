"""Dictionary Utility Functions"""

__author__ = "730700099"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    dict2: dict[str, str] = {}  # create empty dict
    for key in dict1:  # loop through whie=le dict
        if (
            dict1[key] in dict2
        ):  # if output is already in new dict as a key, then raise error
            raise KeyError("More than one of the same key in dictionary")
        dict2[dict1[key]] = (
            key  # if not already in dict, make key new input + vice versa
        )
    return dict2


def favorite_color(colors: dict[str, str]) -> str:
    col: str = ""  # empty to fill with most pop color
    large: int = 0  # int compare color counts
    color: str = ""
    colors2: dict[str, int] = (
        {}
    )  # create new dict to make colors = key for easier count
    for elem in colors:  # go over every key
        color = colors[
            elem
        ]  # color = the string of output value (which is a color name)
        if (
            color in colors2
        ):  # if color name already in new dict then add 1 to vale=ue (keep track count)
            colors2[color] += 1
        else:  # if not alr in new dict then add it and set = to 1
            colors2[color] = 1
    for key in colors2:  # go through new dict for most pop
        if colors2[key] > large:  # if larger than this variable makes it the return
            large = colors2[
                key
            ]  # recodes large ti be this variable so only get large overall
            col = key  # recode to what color is, whole loop takes care of ties
    return col


def count(list1: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}  # empty dict
    for elem in list1:
        if elem in counts:  # if elem already there then just add to the value
            counts[elem] += 1
        else:
            counts[elem] = 1  # if not already there then make value = 1
    return counts


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    alpha_ord: dict[str, list[str]] = {}  # new empty dict
    let: str = ""  # letter for key, used to make process easier
    for word in list1:  # go over every word
        let = word[0].lower()  # make lower case, recode let for every word

        if let in alpha_ord:  # if letter already in dict
            alpha_ord[let].append(
                word
            )  # just append the word to already existing list value
        else:  # letter not in dict
            alpha_ord[let] = []  # make key = to empty list to append stuff
            alpha_ord[let].append(word)  # add the word to the empty list
    return alpha_ord


def update_attendance(d1: dict[str, list[str]], day: str, name: str) -> None:
    if day in d1:  # if day already in the dict
        if name in d1[day]:
            d1[day] = [name]  # if name already there just leave as same name
        else:
            d1[day].append(name)  # just add name to already existing list
    else:
        d1[day] = []  # create key = to list to append stuff
        d1[day].append(name)  # add the name to the empty list
