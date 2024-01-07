import sys
input = sys.stdin.readline

# 2169 로봇 조종하기

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = arr[0][0]
for c in range(1, M):
    dp[0][c] = dp[0][c-1] + arr[0][c]

for r in range(1, N):
    LTR, RTL = arr[r][:], arr[r][:][::-1]
    for c in range(M):
        if c == 0:
            LTR[c] += dp[r-1][c]
            RTL[c] += dp[r-1][M-c-1]
        else:
            LTR[c] += max(LTR[c-1], dp[r-1][c])
            RTL[c] += max(RTL[c-1], dp[r-1][M-c-1])
    for c in range(M):
        dp[r][c] = max(LTR[c], RTL[M-c-1])
print(dp[N-1][M-1])