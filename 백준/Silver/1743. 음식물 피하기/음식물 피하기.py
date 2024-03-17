import sys
input = sys.stdin.readline
from collections import deque

# 1743

N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] += 1

visited = [[0]*M for _ in range(N)]
max_size = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            size = 1
            que = deque([[i, j]])
            while que:
                r, c = que.popleft()
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        que.append([nr, nc])
                        size += 1
            max_size = max(max_size, size)
print(max_size)