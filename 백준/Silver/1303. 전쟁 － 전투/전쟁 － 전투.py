from collections import deque


# 1303

def bfs(start):
    x, y = start
    color = arr[x][y]
    power = 1
    visited[x][y] = 1
    que = deque([[x, y]])
    while que:
        r, c = que.popleft()
        for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == color and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                power += 1
                que.append([nr, nc])
    answer[color] += power ** 2


M, N = map(int, input().split())
arr = [input() for _ in range(N)]
answer = {
    "W": 0,
    "B": 0,
}
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            bfs([i, j])

print(*answer.values())
