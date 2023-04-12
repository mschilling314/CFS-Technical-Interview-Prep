import json
import inspect


def equivalent(exp, actual) -> bool:
    """
    Similar to serialization, needs to be able to give equivalence for non-simple objects.

    Inputs can be two objects of type None, int, float, bool, str, list, tuple, set, or dict.
    """
    if exp is None:
        if actual is None:
            return True
        else:
            return False
    objType = type(exp)
    if not isinstance(actual, objType):
        return False
    if isinstance(exp, (int, float, bool, str)):
        return exp == actual
    if isinstance(exp, (list, tuple)):
        if len(exp) != len(actual):
            return False
        for i in range(len(exp)):
            if not equivalent(exp[i], actual[i]):
                return False
        return True
    if isinstance(exp, set):
        if len(exp) != len(actual):
            return False
        for item in exp:
            if item not in actual:
                return False
        return True
    if isinstance(exp, dict):
        if len(exp) != len(actual):
            return False
        for key in exp.keys():
            if key not in actual:
                return False
            if not equivalent(exp[key], actual[key]):
                return False
        return True
    if inspect.isclass(objType):
        return equivalent(exp.__dict__(), actual.__dict__())
    


def check(func, filename: str) -> None:
    """
    This serves to check a solution in response.py, and should be called from the if/main statement.

    Inputs:
    func: The function that the interviewee will use in response.py.
    filename:  A string representing the relative path to whatever file (usually solutions.json) that has the test cases.

    Output:
    None, prints out a series of strings telling whether you've successfully passed given test cases, and if not what the expected and output solutions are.
    """
    with open(filename) as f:
    # Load the contents of the file into a list
        solutions = json.load(f)
    #solutions = gen.createTests() # need to redefine w/ gen.
    for index, solution in enumerate(solutions):
        inputs = solution[0]
        expected = solution[1]
        output = func(*inputs)
        if equivalent(expected, output):
            print(f"Test case {index} passed!")
        else:
            print(f"Test case {index} failed, expected {expected} but got {output}.")