import sys
input = sys.stdin.readline

# 2406


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    p, q = find(x), find(y)
    parent[max(p, q)] = min(p, q)


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)
cost = [list(map(int, input().split())) for _ in range(N)]
edge = []
for i in range(1, N):
    for j in range(i+1, N):
        edge.append([i+1, j+1, cost[i][j]])
edge.sort(key=lambda x:x[2])
X, K, ans = 0, 0, []
for x, y, c in edge:
    if find(x) != find(y):
        union(x, y)
        ans.append([x, y])
        X += c
        K += 1
        if K == N-1:
            break
print(X, K)
for x, y in ans:
    print(x, y)