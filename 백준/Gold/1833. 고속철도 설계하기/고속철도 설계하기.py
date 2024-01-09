import sys
input = sys.stdin.readline


# 1833 고속철도 설계하기


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
edges = []
parents = [i for i in range(N+1)]
C, M, ans = 0, 0, []
for i in range(N):
    for j in range(i+1, N):
        v = cost[i][j]
        if v < 0:
            C -= v
            if find(i+1) != find(j+1):
                union(i+1, j+1)
            else:
                union(0, min(i+1, j+1))
        else:
            edges.append([i+1, j+1, v])
edges.sort(key=lambda x:x[2])
for x, y, c in edges:
    if find(x) != find(y):
        union(x, y)
        C += c
        M += 1
        ans.append([x, y])

print(C, M)
for a, b in ans:
    print(a, b)