import sys
input = sys.stdin.readline
from collections import deque

# 2468

inf = sys.maxsize
N = int(input())
min_h, max_h = inf, -inf
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    min_h, max_h = min(min_h, min(row)), max(max_h, max(row))
    arr.append(row)
max_area = 1
for h in range(min_h, max_h):
    visited = [[0]*N for _ in range(N)]
    area = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visited[i][j] == 0:
                area += 1
                que = deque([[i, j]])
                visited[i][j] = area
                while que:
                    r, c = que.popleft()
                    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > h and visited[nr][nc] == 0:
                            visited[nr][nc] = visited[r][c]
                            que.append([nr, nc])
    max_area = max(max_area, area)
print(max_area)