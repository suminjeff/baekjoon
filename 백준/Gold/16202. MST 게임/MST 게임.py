import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M, K = map(int, input().split())
edges = [list(map(int, input().split())) + [i+1] for i in range(M)]
ans = [0]*K
for k in range(K):
    parents = [i for i in range(N+1)]
    cost = 0
    for x, y, c in edges:
        p, q = find(x), find(y)
        if p != q:
            union(p, q)
            cost += c
    root = 0
    for p in range(1, N+1):
        if p == parents[p]:
            root += 1
    if root == 1:
        ans[k] = cost
    edges.pop(0)
print(*ans)