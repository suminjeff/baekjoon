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
ans_cheese = -1
while cheese:
    que = deque([[0, 0], [0, M-1], [N-1, 0], [N-1, M-1]])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = visited[0][M-1] = visited[N-1][0] = visited[N-1][M-1] = 1
    melt = []
    while que:
        r, c = que.popleft()
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if arr[nr][nc] == 0:
                    que.append([nr, nc])
                else:
                    melt.append([nr, nc])
    temp_cheese = cheese
    for x, y in melt:
        arr[x][y] = 0
        temp_cheese -= 1
    time += 1
    if temp_cheese == 0:
        print(time)
        print(cheese)
        break
    else:
        cheese = temp_cheese
