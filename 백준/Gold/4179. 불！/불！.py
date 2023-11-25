import sys
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]
ji = deque()
visited = [[0]*C for _ in range(R)]
fire = deque()
fire_visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            visited[i][j] = 1
            ji.append([i, j])
        elif arr[i][j] == 'F':
            fire_visited[i][j] = 1
            fire.append([i, j])

while fire:
    r, c = fire.popleft()
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] in ".J" and fire_visited[nr][nc] == 0:
            fire_visited[nr][nc] = fire_visited[r][c] + 1
            fire.append([nr, nc])
ans = "IMPOSSIBLE"
while ji:
    r, c = ji.popleft()
    if r == 0 or r == R-1 or c == 0 or c == C-1:
        ans = visited[r][c]
        break
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] in ".J" and visited[nr][nc] == 0:
            if fire_visited[nr][nc] == 0 or fire_visited[nr][nc] > visited[r][c]+1:
                visited[nr][nc] = visited[r][c] + 1
                ji.append([nr, nc])

print(ans)