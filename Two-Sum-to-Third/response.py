import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared import checker


def twoSumToThird(arr, third):
    pass


if __name__ == "__main__":
    try:
        checker.check(twoSumToThird, ".\Two-Sum-to-Third\solutions.json")
    except:
        checker.check(twoSumToThird, "./Two-Sum-to-Third/solutions.json")