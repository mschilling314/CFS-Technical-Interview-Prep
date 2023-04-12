import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared import checker


def login(actions):
    pass


if __name__ == "__main__":
    try:
        checker.check(login, ".\Login-Backend\solutions.json")
    except:
        checker.check(login, "./Login-Backend/solutions.json")