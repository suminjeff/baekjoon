import sys
input = sys.stdin.readline

# 11909
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
heap = [[0, 0, 0]]
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            if i == j == 0:
                continue
            else:
                if i == 0:
                    cost = dp[i][j - 1] + (0 if A[i][j - 1] > A[i][j] else A[i][j] - A[i][j - 1] + 1)
                else:
                    cost = dp[i-1][j] + (0 if A[i-1][j] > A[i][j] else A[i][j] - A[i-1][j] + 1)
                dp[i][j] += cost
        else:
            cost1 = dp[i][j-1] + (0 if A[i][j-1] > A[i][j] else A[i][j] - A[i][j-1] + 1)
            cost2 = dp[i-1][j] + (0 if A[i-1][j] > A[i][j] else A[i][j] - A[i-1][j] + 1)
            dp[i][j] += min(cost1, cost2)
print(dp[-1][-1])