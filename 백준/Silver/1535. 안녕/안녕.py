import sys
input = sys.stdin.readline

# 1535


N = int(input())
M = 100
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][M-1])