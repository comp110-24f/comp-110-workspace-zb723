"""Creating a wordle game... YAY!!!"""

__author__ = "730700099"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")  # prompting user to write smth
    if len(word) < 5 or len(word) > 5:  # if less or more than 5 give back error msg
        print("Error: Word must contain 5 characters.")
        exit()  # exits and won't continue to run

    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) < 1 or len(letter) > 1:  # if put it more than 1 char then error
        print("Error: Character must be a single character.")
        exit()  # exits code and won't continue to run

    return letter


def contains_char(
    word: str, letter: str
) -> None:  # Calling the above funcs + making them parameters
    index: int = 0  # Keeps track of the position in the word
    count: int = 0  # Keeping track of how many times it appears
    print("Searching for " + letter + " in " + word)

    if letter == word[index]:
        count += 1  # keep track add if found
        print(letter + " found at index " + str(index))
    index = index + 1
    if letter == word[index]:
        count += 1
        print(letter + " found at index " + str(index))
    index = index + 1
    if letter == word[index]:
        count += 1
        print(letter + " found at index " + str(index))
    index = index + 1
    if letter == word[index]:
        count += 1
        print(letter + " found at index " + str(index))
    index = index + 1
    if letter == word[index]:
        count += 1
        print(letter + " found at index " + str(index))
    if count == 0:  # if none found
        print("No instances of " + (letter) + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + (letter) + " found in " + word)
    else:  # something found
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:  # calling 1 fucntion so don't have to keep calling
    contains_char(input_word(), input_letter())


if __name__ == "__main__":
    main()
