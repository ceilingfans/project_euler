from functools import reduce


def reducer(a, b):
    if not b % 3 or not b % 5:
        return a + b
    return a


def solve():
    return reduce(reducer, range(1000))


if __name__ == "__main__":
    print(solve())
