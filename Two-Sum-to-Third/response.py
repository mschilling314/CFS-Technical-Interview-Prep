import gen


def twoSumToThird(arr, third):
    pass


if __name__ == "__main__":
    solutions = gen.createTests() # need to redefine w/ gen.
    for index, solution in enumerate(solutions):
        inputs = solution[0]
        expected = solution[1]
        output = twoSumToThird(inputs[0], inputs[1])
        if output == expected:
            print(f"Test case {index} passed!")
        else:
            print(f"Test case {index} failed, expected {expected} but got {output}.")

