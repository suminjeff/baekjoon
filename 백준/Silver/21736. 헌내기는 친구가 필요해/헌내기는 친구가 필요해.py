import sys
input = sys.stdin.readline
from collections import deque

# 21736

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

que = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == "I":
            que.append([i, j])
            visited[i][j] = 1


cnt = 0
while que:
    r, c = que.popleft()
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != "X" and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            if arr[nr][nc] == "P":
                cnt += 1
            que.append([nr, nc])
print(cnt if cnt > 0 else "TT")