"""A number guessing game"""

__author__ = "730700099"


def guess_a_number() -> None:
    """User guess a number and it is returned"""
    secret = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
