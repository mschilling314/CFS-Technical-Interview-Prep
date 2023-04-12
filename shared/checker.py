import json


def check(func, filename):
    with open(filename) as f:
    # Load the contents of the file into a list
        solutions = json.load(f)
    #solutions = gen.createTests() # need to redefine w/ gen.
    for index, solution in enumerate(solutions):
        inputs = solution[0]
        expected = solution[1]
        output = func(*inputs)
        if output == expected:
            print(f"Test case {index} passed!")
        else:
            print(f"Test case {index} failed, expected {expected} but got {output}.")

