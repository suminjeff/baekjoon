import sys
input = sys.stdin.readline

from collections import deque

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
adj_l = [[0]*(M+1) for _ in range(M+1)]
nodes = []
start = []
for i in range(N):
    for j in range(N):
        if arr[i][j].isalpha():
            if arr[i][j] == 'S':
                start = [i, j]
            nodes.append([i, j])
edges = []
for i in range(M):
    visited = [[-1]*N for _ in range(N)]
    r, c = nodes[i]
    visited[r][c] = 0
    que = deque([[r, c]])
    while que:
        r, c = que.popleft()
        if arr[r][c].isalpha():
            j = nodes.index([r, c])
            if i != j:
                if adj_l[i][j] == 0:
                    adj_l[i][j] = visited[r][c]
                    edges.append([i, j, visited[r][c]])
                if adj_l[j][i] == 0:
                    adj_l[j][i] = visited[r][c]
                    edges.append([j, i, visited[r][c]])
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1' and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                que.append([nr, nc])
edges.sort(key=lambda x:x[2])
parents = [i for i in range(M+1)]
ans = 0
for x, y, c in edges:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        ans += c

root = 0
for i in range(M+1):
    if i == parents[i]:
        root += 1
if root == 1:
    print(ans)
else:
    print(-1)