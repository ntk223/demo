"""
Bộ test tự động cho TOÀN BỘ thuật toán trong repo.
Chạy:  python -m unittest test_all -v
"""

import unittest

from algorithms import (
    bubble_sort, quick_sort, merge_sort,
    linear_search, binary_search, is_prime,
)
from sorting_extra import insertion_sort, selection_sort, heap_sort, counting_sort
from graphs import bfs, dfs, dijkstra, topological_sort, DisjointSet
from dynamic_programming import fib_memo, fib_tab, lcs, knapsack, coin_change, lis
from strings_algo import is_palindrome, is_anagram, kmp_search, run_length_encode
from math_extra import gcd, lcm, power, sieve

ALL_SORTS = [bubble_sort, quick_sort, merge_sort, insertion_sort, selection_sort, heap_sort]


class TestSorting(unittest.TestCase):
    def test_all_sorts_basic(self):
        data = [42, 7, 19, 3, 88, 25, 1, 56, 13, 7]
        for sort in ALL_SORTS:
            self.assertEqual(sort(data), sorted(data), msg=sort.__name__)

    def test_all_sorts_edge_cases(self):
        cases = [[], [1], [2, 1], [5, 5, 5], [3, -1, 0, -7, 2], [9, 8, 7, 6, 5]]
        for sort in ALL_SORTS:
            for case in cases:
                self.assertEqual(sort(case), sorted(case), msg=sort.__name__)

    def test_sorts_do_not_modify_input(self):
        data = [3, 1, 2]
        snapshot = list(data)
        for sort in ALL_SORTS:
            sort(data)
        self.assertEqual(data, snapshot)

    def test_counting_sort(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])
        self.assertEqual(counting_sort([]), [])
        with self.assertRaises(ValueError):
            counting_sort([1, -2])


class TestSearch(unittest.TestCase):
    def test_linear_and_binary(self):
        data = [42, 7, 19, 3, 88, 25, 1, 56, 13, 7]
        self.assertEqual(linear_search(data, 25), 5)
        self.assertEqual(linear_search(data, 99), -1)
        s = merge_sort(data)
        self.assertEqual(binary_search(s, 25), s.index(25))
        self.assertEqual(binary_search(s, 99), -1)

    def test_is_prime(self):
        for n in (1, 0, -5, 100, 49):
            self.assertFalse(is_prime(n), msg=n)
        for n in (2, 3, 5, 7, 29, 97):
            self.assertTrue(is_prime(n), msg=n)


class TestGraphs(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D", "E"],
            "D": ["F"],
            "E": ["F"],
            "F": [],
        }

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, "A"), ["A", "B", "C", "D", "E", "F"])

    def test_dfs(self):
        self.assertEqual(dfs(self.graph, "A"), ["A", "B", "D", "F", "C", "E"])

    def test_dijkstra(self):
        weighted = {
            "A": [("B", 1), ("C", 4)],
            "B": [("C", 2), ("D", 6)],
            "C": [("D", 3)],
            "D": [],
        }
        self.assertEqual(dijkstra(weighted, "A"), {"A": 0, "B": 1, "C": 3, "D": 6})

    def test_topological_sort(self):
        dag = {"a": ["b"], "b": ["c"], "c": []}
        self.assertEqual(topological_sort(dag), ["a", "b", "c"])
        cyclic = {"a": ["b"], "b": ["a"]}
        self.assertIsNone(topological_sort(cyclic))

    def test_disjoint_set(self):
        dsu = DisjointSet()
        self.assertTrue(dsu.union(1, 2))
        self.assertTrue(dsu.union(3, 4))
        self.assertFalse(dsu.union(1, 2))
        self.assertTrue(dsu.union(2, 4))
        self.assertEqual(dsu.find(1), dsu.find(4))
        self.assertNotEqual(dsu.find(1), dsu.find(5))


class TestDynamicProgramming(unittest.TestCase):
    def test_fibonacci(self):
        for f in (fib_memo, fib_tab):
            self.assertEqual([f(i) for i in range(8)], [0, 1, 1, 2, 3, 5, 8, 13])
            self.assertEqual(f(20), 6765)

    def test_lcs(self):
        self.assertEqual(lcs("ABCBDAB", "BDCABA"), 4)
        self.assertEqual(lcs("abc", "abc"), 3)
        self.assertEqual(lcs("abc", "xyz"), 0)
        self.assertEqual(lcs("", "abc"), 0)

    def test_knapsack(self):
        self.assertEqual(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7), 9)
        self.assertEqual(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5), 7)
        self.assertEqual(knapsack([2], [10], 1), 0)   # không vừa món nào
        self.assertEqual(knapsack([], [], 10), 0)

    def test_coin_change(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)
        self.assertEqual(coin_change([1, 2, 5], 0), 0)

    def test_lis(self):
        self.assertEqual(lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(lis([]), 0)
        self.assertEqual(lis([5, 4, 3, 2, 1]), 1)
        self.assertEqual(lis([1, 2, 3, 4]), 4)


class TestStrings(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

    def test_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Dormitory", "Dirty Room"))
        self.assertFalse(is_anagram("hello", "world"))

    def test_kmp_search(self):
        self.assertEqual(kmp_search("hello world hello", "world"), 6)
        self.assertEqual(kmp_search("aaaa", "aa"), 0)
        self.assertEqual(kmp_search("abc", "xyz"), -1)
        self.assertEqual(kmp_search("abc", ""), 0)

    def test_run_length_encode(self):
        self.assertEqual(run_length_encode("aaabbc"), "a3b2c1")
        self.assertEqual(run_length_encode("aab"), "a2b1")
        self.assertEqual(run_length_encode(""), "")


class TestMath(unittest.TestCase):
    def test_gcd_lcm(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(0, 5), 0)

    def test_power(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(3, 0), 1)
        self.assertEqual(power(5, 3), 125)
        self.assertEqual(power(-2, 3), -8)

    def test_sieve(self):
        self.assertEqual(sieve(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(sieve(2), [2])
        self.assertEqual(sieve(1), [])
        self.assertEqual(len(sieve(100)), 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
