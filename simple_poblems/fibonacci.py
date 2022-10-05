""" functions for calculating fibonacci numbers """
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


if __name__ == '__main__':
    # print('recursive: {}'.format(fibonacci_recursive(40)))
    print('memo: {}'.format(fibonacci_memoization(40)))
    print('memo: {}'.format(fibonacci_automemoization(40)))
