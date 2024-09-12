"""First CQ in COMP110"""

__author__ = "730700099"


def mimic(message: str) -> str:
    """Mimicking the message"""
    return message


# print(mimic(message="yayyy!"))


def main() -> None:
    """Pulls tgt all functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
