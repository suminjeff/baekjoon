import sys
input = sys.stdin.readline

# 2169

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(1, M):
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1, N):
    row = [0]*M
    row[0] = dp[i-1][0] + arr[i][0]

    row_reversed = [0]*M
    row_reversed[M-1] = dp[i-1][M-1] + arr[i][M-1]

    for j in range(1, M):
        # 정방향
        row[j] = max(row[j-1], dp[i-1][j]) + arr[i][j]


    for j in range(M-2, -1, -1):
        # 역방향
        row_reversed[j] = max(row_reversed[j+1], dp[i-1][j]) + arr[i][j]

    for j in range(M):
        dp[i][j] = max(row[j], row_reversed[j])

print(dp[N-1][M-1])