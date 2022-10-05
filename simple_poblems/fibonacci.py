""" functions for calculating fibonacci numbers """
from typing import Generator
from functools import lru_cache
from typing import Dict


def fibonacci_recursive(n: int) -> int:
    """using basic cases"""
    if n < 2:
        return n
    return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)


memo: Dict[int, int] = {0: 0, 1: 1}


def fibonacci_memoization(n: int) -> int:
    """memoization"""
    if n not in memo:
        memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci_automemoization(n: int) -> int:
    """auto-memoization using basic cases"""
    if n < 2:
        return n
    return fibonacci_automemoization(n-2) + fibonacci_automemoization(n-1)


def fibonacci_iteration(n: int) -> int:
    """iteration method"""
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


def fibonacci_iteration_generator(n: int) -> Generator[int, None, None]:
    """generation func iteration method"""
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    # print('recursive: {}'.format(fibonacci_recursive(40)))
    # print('memoization: {}'.format(fibonacci_memoization(40)))
    # print('automemoization: {}'.format(fibonacci_automemoization(40)))
    # print('iteration: {}'.format(fibonacci_iteration(40)))
    for i in fibonacci_iteration_generator(40):
        print(i)
