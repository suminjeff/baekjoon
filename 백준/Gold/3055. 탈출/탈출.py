import sys
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]
water_visited = [[-1]*C for _ in range(R)]
hog_visited = [[-1]*C for _ in range(R)]

water_que = deque()
hog_que = deque()

goal = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == "*":
            water_que.append([i, j])
            water_visited[i][j] = 0
        elif arr[i][j] == "S":
            hog_que.append([i, j])
            hog_visited[i][j] = 0
        elif arr[i][j] == "D":
            goal = [i, j]

# 물 이동
while water_que:
    r, c = water_que.popleft()
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] in "S." and water_visited[nr][nc] == -1:
            water_visited[nr][nc] = water_visited[r][c]+1
            water_que.append([nr, nc])

ans = "KAKTUS"
# 고슴도치 이동
while hog_que:
    r, c = hog_que.popleft()
    if [r, c] == goal:
        ans = hog_visited[r][c]
        break
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] in ".D" and hog_visited[nr][nc] == -1:
            if water_visited[nr][nc] == -1 or water_visited[nr][nc] > hog_visited[r][c]+1:
                hog_visited[nr][nc] = hog_visited[r][c]+1
                hog_que.append([nr, nc])

print(ans)