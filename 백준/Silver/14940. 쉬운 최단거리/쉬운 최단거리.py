import sys
input = sys.stdin.readline

from collections import deque

def bfs(que):
    while que:
        r, c, d = que.popleft()
        for nr, nc in [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                visited[nr][nc] = d
                que.append([nr, nc, d+1])



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            visited[i][j] = 1
            que = deque()
            que.append([i, j, 1])
            bfs(que)
            visited[i][j] = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
for i in range(N):
    print(*visited[i])