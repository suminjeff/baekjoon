import sys
input = sys.stdin.readline

from collections import deque


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*W for _ in range(H)] for _ in range(K+1)]
visited[0][0][0] = 1
min_n = int(10e9)
que = deque()
que.append([0, 0, 0])
while que:
    k, r, c = que.popleft()
    if (r, c) == (H-1, W-1):
        min_n = visited[k][r][c] - 1
        break

    for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
        if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == 0 and visited[k][nr][nc] == 0:
            visited[k][nr][nc] = visited[k][r][c] + 1
            que.append([k, nr, nc])
    if k < K:
        for nr, nc in [[r-1, c-2], [r-2, c-1], [r-2, c+1], [r-1, c+2], [r+1, c+2], [r+2, c+1], [r+2, c-1], [r+1, c-2]]:
            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == 0 and visited[k+1][nr][nc] == 0:
                visited[k+1][nr][nc] = visited[k][r][c] + 1
                que.append([k+1, nr, nc])

if min_n == int(10e9):
    print(-1)
else:
    print(min_n)