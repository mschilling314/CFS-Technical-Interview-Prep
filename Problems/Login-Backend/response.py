import sys
import os
import platform


if platform.system() == "Windows":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))
else:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from shared import checker




def login(actions):
    pass


if __name__ == "__main__":
    checker.check(login, os.path.dirname(__file__))