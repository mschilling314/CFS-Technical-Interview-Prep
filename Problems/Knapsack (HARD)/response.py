import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from shared import checker


def knapsack(items, sack):
    pass


if __name__ == "__main__":
    checker.check(knapsack, os.path.dirname(__file__))