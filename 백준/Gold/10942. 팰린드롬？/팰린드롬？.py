import sys
input = sys.stdin.readline

# 10942 펠린드롬?

N = int(input())
arr = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]
for length in range(N):
    for s in range(N-length):
        e = s+length
        if s == e:
            dp[s][e] = 1
        elif arr[s] == arr[e]:
            if e == s+1:
                dp[s][e] = 1
            elif dp[s+1][e-1] == 1:
                dp[s][e] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])