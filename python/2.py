def solve():
    fibo_prev = 1
    fibo_curr = 2

    ret = 0

    while fibo_curr < 4_000_000:
        if not fibo_curr % 2:
            ret += fibo_curr

        fibo_prev, fibo_curr = fibo_curr, fibo_curr + fibo_prev

    return ret


if __name__ == "__main__":
    print(solve())
