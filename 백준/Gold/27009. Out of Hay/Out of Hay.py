import sys


def solve(n, m, edges):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        p, q = find(x), find(y)
        parent[max(p, q)] = min(p, q)

    edges.sort(key=lambda x:x[2])
    parent = [_ for _ in range(n+1)]

    answer = 0
    cnt = 0
    for a, b, d in edges:
        if find(a) != find(b):
            union(a, b)
            answer = max(answer, d)
            cnt += 1
    if cnt != n-1:
        return -1
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    EDGES = [list(map(int, input().split())) for _ in range(M)]
    ANSWER = solve(N, M, EDGES)
    print(ANSWER)