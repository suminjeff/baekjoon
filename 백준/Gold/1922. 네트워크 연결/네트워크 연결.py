import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N, M = [int(input()) for _ in range(2)]
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])

parents = [i for i in range(N+1)]
ans = 0
for x, y, cost in edges:
    p, q = find(x), find(y)
    if p == q:
        continue
    union(p, q)
    ans += cost

print(ans)