import sys
from collections import deque

# 1926

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
max_size = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            size = 1
            que = deque([[i, j]])
            while que:
                r, c = que.popleft()
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        size += 1
                        que.append([nr, nc])
            max_size = max(max_size, size)
print(cnt)
print(max_size)