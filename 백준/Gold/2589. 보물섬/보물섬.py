import sys
input = sys.stdin.readline
from collections import deque

def treasure(r, c):
    global max_distance
    que = deque()
    que.append([0, r, c])
    while que:
        depth, r, c = que.popleft()
        max_distance = max(max_distance, depth)
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c]+1
                que.append([depth+1, nr, nc])


N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
max_distance = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            treasure(i, j)
print(max_distance)