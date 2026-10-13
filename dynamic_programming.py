"""
Quy hoạch động (Dynamic Programming)
====================================
"""

from bisect import bisect_left
from functools import lru_cache


def fib_memo(n):
    """Fibonacci bằng đệ quy có nhớ (memoization) — O(n)."""
    @lru_cache(maxsize=None)
    def f(k):
        if k < 2:
            return k
        return f(k - 1) + f(k - 2)
    return f(n)


def fib_tab(n):
    """Fibonacci bằng bảng phương án (tabulation) — O(n) thời gian, O(1) bộ nhớ."""
    if n < 2:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def lcs(a, b):
    """Độ dài chuỗi con chung dài nhất (Longest Common Subsequence) — O(m * n)."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def knapsack(weights, values, capacity):
    """Balo 0/1 — O(n * capacity). Trả về giá trị lớn nhất có thể mang.
    Yêu cầu: weights[i] > 0."""
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for c in range(capacity, weights[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i])
    return dp[capacity]


def coin_change(coins, amount):
    """Đổi tiền: số xu ít nhất để đủ amount — O(amount * len(coins)).
    Trả về -1 nếu không thể đổi."""
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
    return dp[amount] if dp[amount] != INF else -1


def lis(nums):
    """Độ dài dãy con tăng dài nhất — O(n log n) (patience sorting)."""
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
