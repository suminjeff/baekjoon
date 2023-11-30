import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheese = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheese += 1

time = 0
while cheese:
    que = deque([[0, 0], [0, M-1], [N-1, 0], [N-1, M-1]])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = visited[0][M-1] = visited[N-1][0] = visited[N-1][M-1] = 1
    melt = []
    while que:
        r, c = que.popleft()
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    que.append([nr, nc])
                elif arr[nr][nc] == 1:
                    visited[nr][nc] += 1
                    if visited[nr][nc] >= 2 and ([nr, nc] not in melt):
                        melt.append([nr, nc])
    for x, y in melt:
        arr[x][y] = 0
        cheese -= 1
    time += 1

print(time)