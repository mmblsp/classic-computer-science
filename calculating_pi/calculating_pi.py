"""leibniz formula calculate pi"""


def calculate_pi(n_terms: int) -> float:
    """calculate pi"""
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi_value: float = 0.0
    for _ in range(n_terms):
        pi_value += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi_value


if __name__ == "__main__":
    print(calculate_pi(10000000))
