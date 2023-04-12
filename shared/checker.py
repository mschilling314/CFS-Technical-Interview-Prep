import json
import inspect


def equivalent(exp, actual) -> bool:
    """
    Similar to serialization, needs to be able to give equivalence for non-simple objects.

    Inputs can be two objects of type None, int, float, bool, str, list, tuple, set, dict, or class instance.
    """
    if (exp is None and actual is not None) or (exp is not None and actual is None):
        return False
    elif exp is None:
        return True
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
    if isinstance(objType, set):
        return equivalent(list(exp), list(actual))
    if isinstance(objType, dict):
        if len(exp) != len(actual):
            return False
        expKeys = exp.keys()
        if not equivalent(expKeys, actual.keys()):
            return False
        for k in exp.keys():
            if not equivalent(expKeys, actual[k]):
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

