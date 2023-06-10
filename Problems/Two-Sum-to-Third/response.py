import sys
import platform
import os


if platform.system() == "Windows":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))
else:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from shared import checker


def twoSumToThird(arr, third):
    pass


if __name__ == "__main__":
    checker.check(twoSumToThird, os.path.dirname(__file__))