from collections import deque


def bfs(start: list):
    que = deque([start])
    while que:
        r, c = que.popleft()
        for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc] == 0 and arr[nr][nc] == "#":
                visited[nr][nc] = 1
                que.append([nr, nc])


T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    arr = [input() for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and visited[i][j] == 0:
                visited[i][j] = 1
                bfs([i, j])
                cnt += 1
    print(cnt)
