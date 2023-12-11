import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N, P = map(int, input().split())
parents = [i for i in range(N+1)]
cost = [int(input()) for _ in range(N)]
edges = [list(map(int, input().split())) for _ in range(P)]
for i in range(len(edges)):
    x, y, c = edges[i]
    edges[i][2] += cost[x-1] + cost[y-1] + c
edges.sort(key=lambda x:x[2])
start = edges[0]
ans = 0
for x, y, c in edges:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        ans += c

print(ans + min(cost))