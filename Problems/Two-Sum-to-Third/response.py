import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))
from shared import checker


def twoSumToThird(arr, third):
    pass


if __name__ == "__main__":
    solution_path = os.path.dirname(__file__)
    checker.check(twoSumToThird, solution_path)