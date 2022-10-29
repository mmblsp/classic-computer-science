""" functions for calculating fibonacci numbers """

from functools import lru_cache
from typing import Dict
from typing import Generator


def fibonacci_recursive(number: int) -> int:
    """using basic cases"""
    if number < 2:
        return number
    return fibonacci_recursive(number-2) + fibonacci_recursive(number-1)


memo: Dict[int, int] = {0: 0, 1: 1}


def fibonacci_memoization(number: int) -> int:
    """memoization"""
    if number not in memo:
        memo[number] = fibonacci_memoization(number-1) + fibonacci_memoization(number-2)
    return memo[number]


@lru_cache(maxsize=None)
def fibonacci_automemoization(number: int) -> int:
    """auto-memoization using basic cases"""
    if number < 2:
        return number
    return fibonacci_automemoization(number-2) + fibonacci_automemoization(number-1)


def fibonacci_iteration(number: int) -> int:
    """iteration method"""
    if number == 0:
        return number
    lst: int = 0
    nxt: int = 1
    for _ in range(1, number):
        lst, nxt = nxt, lst + nxt
    return nxt


def fibonacci_iteration_generator(number: int) -> Generator[int, None, None]:
    """generation func iteration method"""
    yield 0
    if number > 0:
        yield 1
    lst: int = 0
    nxt: int = 1
    for _ in range(1, number):
        lst, nxt = nxt, lst + nxt
        yield nxt


if __name__ == '__main__':
    # print('recursive: {}'.format(fibonacci_recursive(40)))
    # print('memoization: {}'.format(fibonacci_memoization(40)))
    # print('automemoization: {}'.format(fibonacci_automemoization(40)))
    # print('iteration: {}'.format(fibonacci_iteration(40)))
    for i in fibonacci_iteration_generator(40):
        print(i)
