"""
Thuật toán cơ bản (Basic Algorithms)
====================================
Gồm các thuật toán sắp xếp và tìm kiếm kinh điển.

Chạy thử:
    python algorithms.py
"""

# ----------------------------- SẮP XẾP -----------------------------

def bubble_sort(arr):
    """Sắp xếp nổi bọt — O(n^2). Đơn giản, dễ hiểu."""
    a = list(arr)
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:  # đã có thứ tự thì dừng sớm
            break
    return a


def quick_sort(arr):
    """Sắp xếp nhanh — O(n log n) trung bình, chia để trị (divide & conquer)."""
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def merge_sort(arr):
    """Sắp xếp trộn — O(n log n), ổn định (stable)."""
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ----------------------------- TÌM KIẾM -----------------------------

def linear_search(arr, target):
    """Tìm kiếm tuyến tính — O(n). Trả về chỉ số đầu tiên tìm thấy, -1 nếu không có."""
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def binary_search(arr, target):
    """Tìm kiếm nhị phân — O(log n). Yêu cầu mảng ĐÃ SẮP XẾP TĂNG DẦN."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def is_prime(n):
    """Kiểm tra số nguyên tố — O(sqrt(n)) bằng cách chỉ xét đến căn bậc hai."""
    if n < 2:
        return False
    if n < 4:
        return True  # 2, 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ----------------------------- DEMO -----------------------------

if __name__ == "__main__":
    data = [42, 7, 19, 3, 88, 25, 1, 56, 13, 7]

    print("Dữ liệu gốc      :", data)
    print("Bubble sort      :", bubble_sort(data))
    print("Quick sort       :", quick_sort(data))
    print("Merge sort       :", merge_sort(data))

    sorted_data = merge_sort(data)
    target = 25
    print(f"\nTìm {target} (tuyến tính): chỉ số", linear_search(data, target))
    print(f"Tìm {target} (nhị phân)  : chỉ số", binary_search(sorted_data, target))
    print(f"Tìm 100 (nhị phân)       : chỉ số", binary_search(sorted_data, 100))

    primes = [x for x in range(2, 30) if is_prime(x)]
    print("\nSố nguyên tố < 30   :", primes)
