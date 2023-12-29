import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]
    dp[r][c] = 1
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < N and bamboo[r][c] < bamboo[nr][nc]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc)+1)
    return dp[r][c]


N = int(input())
bamboo = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            ans = max(ans, dfs(i, j))
print(ans)