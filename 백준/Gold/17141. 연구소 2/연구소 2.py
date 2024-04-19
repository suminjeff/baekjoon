import sys
from collections import deque

# 1956


def pick(n, r):
    for i in range(1, 1 << n):
        subset = []
        for j in range(i):
            if i & (1 << j):
                subset.append(j)
        if len(subset) == r:
            spread_virus(subset)


def spread_virus(spots):
    global min_time
    visited = [[-1]*N for _ in range(N)]
    que = deque()
    for i in spots:
        r, c = virus_spots[i]
        visited[r][c] = 0
        que.append([r, c])

    time = 0
    spaces = M
    while que:
        r, c = que.popleft()
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                que.append([nr, nc])
                time = max(time, visited[nr][nc])
                spaces += 1
    if spaces == empty_spaces:
        min_time = min(min_time, time)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_spots = []
empty_spaces = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_spots.append([i, j])
            empty_spaces += 1
        if arr[i][j] == 0:
            empty_spaces += 1

inf = sys.maxsize
min_time = inf
pick(len(virus_spots), M)

print(min_time if min_time != inf else -1)