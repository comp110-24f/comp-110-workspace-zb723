"""This program will help you plan a cozy tea party."""

__author__: str = "730700099"


def tea_bags(people: int) -> int:
    """Find # of tea bags needed based off # of people."""
    return people * 2


def treats(people: int) -> int:
    """Calculate # of treats needed based off # of people."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Figure out how much the tea party costs based off treats and tea bags."""
    return (tea_count * 0.5) + (treat_count * 0.75)


def main_planner(guests: int) -> None:
    """To bring all the fucntions together."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))) + ".")
    return None


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
