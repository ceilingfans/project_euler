from functools import reduce

def solve():
    return reduce(lambda a, b: a + b if not b % 3 or not b % 5 else a, range(1000))


if __name__ == "__main__":
    print(solve())
