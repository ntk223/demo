"""
Thuật toán xâu ký tự (String Algorithms)
========================================
"""


def is_palindrome(s):
    """Kiểm tra đối xứng (bỏ qua khoảng trắng/dấu và không phân biệt hoa thường) — O(n)."""
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


def is_anagram(a, b):
    """Kiểm tra hai chuỗi có phải hoán vị của nhau (bỏ khoảng trắng) — O(n log n)."""
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())


def kmp_search(text, pattern):
    """Tìm kiếm Knuth–Morris–Pratt — O(n + m).
    Trả về chỉ số xuất hiện đầu tiên của pattern trong text, -1 nếu không có."""
    if not pattern:
        return 0
    # Bước 1: bảng tiền tố (failure function)
    lps = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k > 0 and pattern[i] != pattern[k]:
            k = lps[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        lps[i] = k
    # Bước 2: quét văn bản
    k = 0
    for i, ch in enumerate(text):
        while k > 0 and ch != pattern[k]:
            k = lps[k - 1]
        if ch == pattern[k]:
            k += 1
            if k == len(pattern):
                return i - k + 1
    return -1


def run_length_encode(s):
    """Mã hóa RLE: 'aaabbc' -> 'a3b2c1'."""
    if not s:
        return ""
    out = []
    count = 1
    for prev, cur in zip(s, s[1:]):
        if cur == prev:
            count += 1
        else:
            out.append(f"{prev}{count}")
            count = 1
    out.append(f"{s[-1]}{count}")
    return "".join(out)
