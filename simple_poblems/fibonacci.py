''' functions for calculating fibonacci numbers '''

def fibonacci_recursive(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

if __name__ == '__main__':
    print(fibonacci_recursive(40))