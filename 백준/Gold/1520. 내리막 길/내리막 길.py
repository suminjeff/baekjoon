import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(r, c):
    global ans
    if (r, c) == (M-1, N-1):
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    cnt = 0
    for nr, nc in [[r-1, c], [r, c+1], [r, c-1], [r+1, c]]:
        if 0 <= nr < M and 0 <= nc < N and arr[r][c] > arr[nr][nc]:
            cnt += dfs(nr, nc)
    dp[r][c] = cnt
    return dp[r][c]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
print(dfs(0, 0))