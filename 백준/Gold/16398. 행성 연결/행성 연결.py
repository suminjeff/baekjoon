import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N = int(input())
parents = [i for i in range(N)]
cost = [list(map(int, input().split())) for _ in range(N)]
edges = []
for i in range(N):
    for j in range(i+1, N):
        edges.append([i, j, cost[i][j]])
edges.sort(key=lambda x:x[2])
ans = 0
for x, y, c in edges:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        ans += c
print(ans)