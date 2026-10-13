"""
Thuật toán đồ thị (Graph Algorithms)
====================================
Đồ thị biểu diễn bằng danh sách kề: {node: [neighbors]}.
Với Dijkstra: {node: [(neighbor, weight), ...]}.
"""

import heapq
from collections import deque


def bfs(graph, start):
    """Duyệt theo chiều rộng — O(V + E). Trả về thứ tự các đỉnh thăm được."""
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph.get(node, []):
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order


def dfs(graph, start):
    """Duyệt theo chiều sâu (đệ quy) — O(V + E)."""
    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)
        for nb in graph.get(node, []):
            if nb not in visited:
                visit(nb)

    visit(start)
    return order


def dijkstra(graph, start):
    """Đường đi ngắn nhất từ start (trọng số >= 0) — O((V + E) log V)."""
    dist = {start: 0}
    heap = [(0, start)]
    visited = set()
    while heap:
        d, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        for nb, w in graph.get(node, []):
            nd = d + w
            if nd < dist.get(nb, float("inf")):
                dist[nb] = nd
                heapq.heappush(heap, (nd, nb))
    return dist


def topological_sort(graph):
    """Sắp xếp tôpô (thuật toán Kahn). Trả về None nếu đồ thị có chu trình."""
    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] = indegree.get(v, 0) + 1
    queue = deque(u for u in indegree if indegree[u] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return order if len(order) == len(indegree) else None


class DisjointSet:
    """Union–Find (tập hợp rời rạc): nén đường đi + hợp nhất theo hạng."""

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, x, y):
        """Hợp nhất 2 tập. Trả về False nếu x, y đã cùng tập."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
