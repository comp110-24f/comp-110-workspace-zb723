"""idk what this does yet"""

__author__ = "730700099"


def concat(w1: str, w2: str) -> str:
    z: str = w1 + w2  # local variable to add tgt
    return z


word1: str = "happy"  # global variables for function
word2: str = "tuesday"

print(concat(word1, word2))

if __name__ == "__main__":  # runs when file runs as script bit not when imported
    concat(word1, word2)
