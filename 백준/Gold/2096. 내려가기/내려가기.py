import sys
input = sys.stdin.readline
n = int(input())

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(n):
    a, b, c = map(int, input().rstrip().split())
    if i == 0:
        max_dp = [a, b, c]
        min_dp = [a, b, c]
    else:
        temp_max = max_dp[:]
        max_dp[0] = max(temp_max[:2]) + a
        max_dp[1] = max(temp_max) + b
        max_dp[2] = max(temp_max[1:]) + c

        temp_min = min_dp[:]
        min_dp[0] = min(temp_min[:2]) + a
        min_dp[1] = min(temp_min) + b
        min_dp[2] = min(temp_min[1:]) + c

print(max(max_dp), min(min_dp))