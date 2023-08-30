"""
Created at 2023/8/30


"""
import functools


@functools.lru_cache
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def fib1(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
    return a


@functools.lru_cache
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    # 0 1 1 2 3 5 8 13 21
    # ret = fib(400)
    # print(ret)
    # print(factorial(3))

    print(fib1(400))
