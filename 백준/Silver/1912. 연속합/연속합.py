import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
start, end = 0, 1
dp = [0]*N
dp[start] = arr[start]
ans = dp[start]
for i in range(1, N):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    ans = max(dp[i], ans)
print(ans)
