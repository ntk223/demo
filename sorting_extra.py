"""
Thuật toán sắp xếp bổ sung (More Sorting Algorithms)
====================================================
Bổ sung cho algorithms.py: insertion, selection, heap, counting.
"""

def insertion_sort(arr):
    """Sắp xếp chèn — O(n^2), rất nhanh với mảng gần như đã có thứ tự."""
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr):
    """Sắp xếp chọn — O(n^2), số lần hoán đổi ít nhất trong các sort đơn giản."""
    a = list(arr)
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
    return a


def heap_sort(arr):
    """Sắp xếp vun đống — O(n log n), in-place, không đệ quy."""
    a = list(arr)
    n = len(a)

    def sift_down(start, end):
        # Vun xuống trong đoạn a[start..end]
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                break

    # Bước 1: xây max-heap
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n - 1)
    # Bước 2: rút từng phần tử lớn nhất ra cuối mảng
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(0, end - 1)
    return a


def counting_sort(arr):
    """Sắp xếp đếm — O(n + k), chỉ dùng cho số nguyên không âm."""
    if not arr:
        return []
    if any(x < 0 for x in arr):
        raise ValueError("counting_sort chỉ hỗ trợ số nguyên không âm")
    counts = [0] * (max(arr) + 1)
    for x in arr:
        counts[x] += 1
    result = []
    for value, c in enumerate(counts):
        result.extend([value] * c)
    return result
