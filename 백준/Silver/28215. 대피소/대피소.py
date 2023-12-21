import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, K = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(N)]
X, Y = [], []
for i in range(N):
    x, y = houses[i]
    X.append([x, i])
    Y.append([y, i])
adj_m = [[0]*N for _ in range(N)]
for i in range(N):
    x1, hx1 = X[i]
    y1, hy1 = Y[i]
    for j in range(i+1, N):
        x2, hx2 = X[j]
        y2, hy2 = Y[j]
        dx = abs(x1-x2)
        dy = abs(y1-y2)
        adj_m[hx1][hx2] += dx
        adj_m[hx2][hx1] += dx
        adj_m[hy1][hy2] += dy
        adj_m[hy2][hy1] += dy

edges = []
for i in range(N):
    for j in range(i+1, N):
        edges.append([i, j, adj_m[i][j]])
edges.sort(key=lambda x:x[2])
parents = [i for i in range(N)]

if K > 1:
    ans = 0
    cnt = 0
    for x, y, c in edges:
        if cnt == N-K:
            break
        p, q = find(x), find(y)
        if p != q:
            union(p, q)
            ans = max(ans, c)
            cnt += 1
else:
    ans = int(1e9)
    for i in range(N):
        max_len = 0
        for j in range(N):
            if i != j:
                max_len = max(max_len, adj_m[i][j])
        ans = min(ans, max_len)
print(ans)
