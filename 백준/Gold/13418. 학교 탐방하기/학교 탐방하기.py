import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N, M = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(M+1)]
edges_asc = list(sorted(edges, key=lambda x:x[2]))
edges_desc = list(reversed(edges_asc))

parents = [i for i in range(N+1)]
asc = 0
for x, y, c in edges_asc:
    p, q = find(x), find(y)
    if p != q:
        union(x, y)
        asc += 1-c

parents = [i for i in range(N+1)]
desc = 0
for x, y, c in edges_desc:
    p, q = find(x), find(y)
    if p != q:
        union(x, y)
        desc += 1-c

ans = asc**2 - desc**2
print(ans)