import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 1. bfs를 위한 큐 생성
que = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                que.append((k, i, j))

# 2. bfs 실행
while que:
    h, r, c = que.popleft()
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[h][nr][nc] == 0:
            arr[h][nr][nc] = arr[h][r][c] + 1
            que.append((h, nr, nc))
    for dh in [1, -1]:
        nh = h + dh
        if 0 <= nh < H and arr[nh][r][c] == 0:
            arr[nh][r][c] = arr[h][r][c] + 1
            que.append((nh, r, c))

time = 0
flag = False
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                flag = True
            time = max(time, arr[k][i][j])
if flag:
    print(-1)
else:
    print(time-1)
