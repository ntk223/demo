"""
Thuật toán quay lui (Backtracking)
==================================
"""

def tower_of_hanoi(n, source="A", auxiliary="B", target="C"):
    """Tháp Hà Nội: trả về danh sách bước di chuyển 'X->Y' — O(2^n)."""
    moves = []

    def solve(k, src, aux, dst):
        if k == 0:
            return
        solve(k - 1, src, dst, aux)   # chuyển k-1 đĩa sang cột phụ
        moves.append(f"{src}->{dst}") # chuyển đĩa lớn nhất sang đích
        solve(k - 1, aux, src, dst)   # chuyển k-1 đĩa từ phụ sang đích

    solve(n, source, auxiliary, target)
    return moves


def n_queens(n):
    """Xếp n quân hậu trên bàn n x n sao cho không quân nào tấn công nhau.
    Trả về danh sách cột theo từng hàng (placement[r] = cột của hậu ở hàng r),
    hoặc None nếu không có lời giải."""
    cols, diag1, diag2 = set(), set(), set()
    placement = []

    def place(r):
        if r == n:
            return True
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            cols.add(c); diag1.add(r - c); diag2.add(r + c)
            placement.append(c)
            if place(r + 1):
                return True
            cols.discard(c); diag1.discard(r - c); diag2.discard(r + c)
            placement.pop()
        return False

    return placement if place(0) else None


def permutations(items):
    """Sinh tất cả hoán vị của một danh sách — O(n!)."""
    result = []
    used = [False] * len(items)
    current = []

    def backtrack():
        if len(current) == len(items):
            result.append(list(current))
            return
        for i, x in enumerate(items):
            if used[i]:
                continue
            used[i] = True
            current.append(x)
            backtrack()
            current.pop()
            used[i] = False

    backtrack()
    return result


def subsets(items):
    """Sinh tất cả tập con (bao gồm tập rỗng) — O(2^n)."""
    result = []
    current = []

    def backtrack(start):
        result.append(list(current))
        for i in range(start, len(items)):
            current.append(items[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result
