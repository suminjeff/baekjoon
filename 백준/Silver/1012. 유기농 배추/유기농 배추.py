import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(r, c, v):
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
            if not visited[nr][nc]:
                visited[nr][nc] = v
                dfs(nr, nc, v)


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    visited = [[0]*M for _ in range(N)]
    v = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                v += 1
                visited[i][j] = v
                dfs(i, j, v)
    print(v)
