"""YAYYYY!!! MAKING WORDLE!"""

__author__ = "730700099"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    answr: bool = False  # if cond returns answr (true) then exit
    while turns <= int(6) and (not answr):
        print(f"=== Turn {turns}/6 ===")  # keep track of turns
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if secret == guess:  # won but with multiple turns
            print(f"You won in {turns}/6 turns!")
            answr = True  # exits
        turns = turns + 1  # add turns to keep tack
    if turns > 6 and (not answr):  # ran out of turns
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(wrd_len: int) -> str:
    guess: str = input(f"Enter a {wrd_len} character word:  ")
    while len(guess) != wrd_len:  # not equal then go through while loop
        guess = input(
            f"That wasn't {wrd_len} chars! Try again: "
        )  # change so the while loop don't repeat and uses new input
    return guess  # return what person put back to them


def contains_char(word: str, char: str) -> bool:
    """To search through every character of word and find matches"""
    assert len(char) == 1  # char has to be 1 word or eon't run
    idx: int = 0  # track place in word
    count: int = 0  # keep track if letter shows up or not
    while idx <= len(word) - 1:  # creates a limit so no infinite loop
        if word[idx] == char:
            count += 1  # used later for bool return
        idx += 1
    if count > 0:  # if count has > 0 instances of char then True
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """strings of equal len, using emojis to indicate correct/wrong guesses"""
    assert len(guess) == len(secret)
    idx: int = 0
    color: str = ""  # empty str so can add colors/emojis to it
    WHITE_BOX: str = "\U00002B1C"  # Emojis yayyy
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while idx < len(secret):  # set limit so no infinite loop
        if guess[idx] == secret[idx]:  # if both letters the same enter if statement
            color = color + GREEN_BOX  # Add green box emoji to the color string
        if guess[idx] != secret[idx]:  # if doesn't = then enter this
            if contains_char(
                secret, guess[idx]
            ):  # if this returns true, put yellow box
                color = color + YELLOW_BOX
            else:
                color = color + WHITE_BOX  # if not letter found put white
        idx += 1  # increase idx to keep loop going

    return color


if __name__ == "__main__":
    main(secret="codes")
