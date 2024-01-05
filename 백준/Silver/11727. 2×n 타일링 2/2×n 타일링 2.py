import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
dp[1] = 1
for i in range(2, N+1):
    if i == 2:
        dp[2] = 3
    else:
        dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[N]%10007)