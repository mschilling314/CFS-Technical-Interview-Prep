import json
import random


def generate_fibonacci_list(n: int=1000) -> list:
    res = [0, 1]
    for x in range(2, n):
        res.append(res[x-2] + res[x-1])
    return res


def create_tests(n: int=10):
    fib = generate_fibonacci_list()
    # print(fib[0:10])
    used = set()
    used.add(-1)
    examples = []
    for _ in range(n):
        inp = -1
        while inp in used:
            inp = random.randint(0, 100)
        used.add(inp)
        expected = fib[inp]
        examples.append([[inp], expected])
    return examples


        

if __name__ == "__main__":
    filename = "./Problems/Fibonacci/solutions.json"
    tests = create_tests(n=25)
    with open(filename, 'w') as f:
        json.dump(tests, f, indent=4)
