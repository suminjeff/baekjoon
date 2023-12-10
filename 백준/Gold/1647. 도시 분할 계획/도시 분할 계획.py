import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parents = [i for i in range(N + 1)]

res = []
for x, y, cost in edges:
    x, y = find(x), find(y)
    if x != y:
        union(x, y)
        res.append(cost)

ans = sum(res) - max(res)
print(ans)