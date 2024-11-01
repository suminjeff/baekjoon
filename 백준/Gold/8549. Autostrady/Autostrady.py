import sys


def solve(n, m, edges):
    edges.sort(key=lambda x:x[2])
    parent = [_ for _ in range(n+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        p, q = find(x), find(y)
        parent[max(p, q)] = min(p, q)

    mst = 0
    max_v = 0
    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
            mst += c
            max_v = max(max_v, c)

    return max_v


if __name__ == '__main__':
    N, M = map(int, input().split())
    EDGES = [list(map(int, input().split())) for _ in range(M)]
    ANSWER = solve(N, M, EDGES)
    print(ANSWER)