import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N = int(input())
cost_dig = [int(input()) for _ in range(N)]
cost_connect = [list(map(int, input().split())) for _ in range(N)]
edges = []
for i in range(N):
    edges.append([0, i+1, cost_dig[i]])
    for j in range(i+1, N):
        edges.append([i+1, j+1, cost_connect[i][j]])
edges.sort(key=lambda x:x[2])

parents = [i for i in range(N+1)]
ans = 0
cnt = 0
for x, y, c in edges:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        ans += c
        cnt += 1
    if cnt == N:
        break
print(ans)