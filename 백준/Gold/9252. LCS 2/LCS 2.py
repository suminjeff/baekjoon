import sys
input = sys.stdin.readline
# 9252

A, B = [input().rstrip() for _ in range(2)]
N, M = len(A), len(B)
dp = [[[0, ""]]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = [dp[i-1][j-1][0]+1, dp[i-1][j-1][1]+A[i-1]]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans1, ans2 = dp[-1][-1]
print(ans1)
if ans1 > 0:
    print(ans2)