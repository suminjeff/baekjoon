import sys
input = sys.stdin.readline
# 27945 슬슬 가지를 먹지 않으면 죽는다


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
day = 1
parents = [i for i in range(N+1)]
for x, y, d in edges:
    if day == d and find(x) != find(y):
        day += 1
        union(x, y)
print(day)