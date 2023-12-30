import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

max_length = max(dp)
print(max_length)
max_idx = dp.index(max_length)
lis = []
while max_idx >= 0:
    if dp[max_idx] == max_length:
        lis.append(arr[max_idx])
        max_length -= 1
    max_idx -= 1
print(*reversed(lis))
