"""
Thuật toán toán học (Math Algorithms)
=====================================
"""


def gcd(a, b):
    """Ước chung lớn nhất — thuật toán Euclid — O(log min(a, b))."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Bội chung nhỏ nhất."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def power(base, exp):
    """Lũy thừa nhanh (binary exponentiation) — O(log exp)."""
    if exp < 0:
        raise ValueError("exp phải >= 0")
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result


def sieve(limit):
    """Sàng Eratosthenes: trả về mọi số nguyên tố <= limit — O(n log log n)."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return [i for i, ok in enumerate(is_prime) if ok]
