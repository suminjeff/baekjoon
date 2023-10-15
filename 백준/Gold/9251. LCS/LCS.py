import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

l1, l2 = len(s1), len(s2)

dp = [0]*l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < dp[j]:
            cnt = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = cnt + 1
print(max(dp))