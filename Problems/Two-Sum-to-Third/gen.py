import json
import random


# A few constants that can be tweaked
THIRD_MAX = 10000
ARR_MAX = 100
DEFAULT_TESTS = 10


def createInput(expected: bool):
    """
    Given whether the expected value is true or false returns an array and value.
    """
    third = random.randint(0, THIRD_MAX)
    first = random.randint(0, third)
    second = third - first
    arr = [first]
    for i in range(random.randint(0, ARR_MAX)):
        arr.append(random.randint(0, 2*THIRD_MAX))
    if expected:
        arr.append(second)
    else:
        for i in arr:
            second = third - i
            while second in arr:
                arr.remove(second)
            if second * 2 == third:
                arr.append(second)
    random.shuffle(arr)
    return arr, third


def createTests(numTests: int=DEFAULT_TESTS):
    tests = []
    correctTests = numTests//2
    for _ in range(correctTests):
        inputs = createInput(True)
        tests.append([inputs, True])
    for _ in range(correctTests, numTests):
        inputs = createInput(False)
        tests.append([inputs, False])
    random.shuffle(tests)
    return tests


def printTests(tests):
    for i in range(len(tests)):
        print(f"arr: {tests[i][0][0]}")
        print(f"third: {tests[i][0][1]}")
        print(f"expected: {tests[i][1]}")


if __name__ == "__main__":
    filename = "./Two-Sum-to-Third/solutions.json"
    tests = createTests()
    with open(filename, 'w') as f:
        json.dump(tests, f, indent=4)
