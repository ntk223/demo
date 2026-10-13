# Demo — Bộ sưu tập thuật toán

Các thuật toán kinh điển bằng Python, kèm **bộ test tự động** (`unittest`).

## Cấu trúc

| File | Nội dung |
|------|----------|
| `algorithms.py` | Bubble/Quick/Merge sort, Linear/Binary search, kiểm tra số nguyên tố |
| `sorting_extra.py` | Insertion/Selection/Heap/Counting sort |
| `graphs.py` | BFS, DFS, Dijkstra, Topological sort (Kahn), Union–Find |
| `dynamic_programming.py` | Fibonacci (memo + tabulation), LCS, Knapsack 0/1, Đổi tiền, LIS |
| `strings_algo.py` | Palindrome, Anagram, KMP, Run-length encoding |
| `math_extra.py` | GCD/LCM (Euclid), Lũy thừa nhanh, Sàng Eratosthenes |
| `test_all.py` | Bộ test `unittest` cho toàn bộ thuật toán trên |

## Chạy demo

```bash
python algorithms.py
```

## Chạy toàn bộ test

```bash
python -m unittest test_all -v
```
