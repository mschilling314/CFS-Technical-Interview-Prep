import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from shared import checker


def fibonacci(n):
    pass


if __name__ == "__main__":
    checker.check(fibonacci, os.path.dirname(__file__))