import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    if x in generators and y in generators:
        return "FALSE"
    else:
        if x not in generators and y not in generators:
            parents[max(x, y)] = min(x, y)
        elif x in generators:
            parents[y] = x
        elif y in generators:
            parents[x] = y
        return "TRUE"


N, M, K = map(int, input().split())
generators = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
parents = [i for i in range(N+1)]
ans = 0
for x, y, cost in edges:
    p, q = find(x), find(y)
    if p != q:
        if union(p, q) == "TRUE":
            ans += cost

print(ans)