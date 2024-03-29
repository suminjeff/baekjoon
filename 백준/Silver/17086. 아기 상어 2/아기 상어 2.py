import sys
input = sys.stdin.readline

# 17086

from collections import deque


def bfs(start):
    x, y = start
    visited[x][y] = 0
    que = deque([[x, y]])

    while que:
        r, c = que.popleft()
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1], [r-1, c-1], [r-1, c+1], [r+1, c-1], [r+1, c+1]]:
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] > visited[r][c] + 1:
                visited[nr][nc] = visited[r][c] + 1
                que.append([nr, nc])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[51]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs([i, j])

safety = 0
for i in range(N):
    for j in range(M):
        safety = max(safety, visited[i][j])
print(safety)
