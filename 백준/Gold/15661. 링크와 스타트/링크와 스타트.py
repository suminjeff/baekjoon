import sys
input = sys.stdin.readline

# 09:23 15661

N = int(input())
S = [[0]*N for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        S[i][j] += arr[j]
        S[j][i] += arr[j]

ans = sys.maxsize
for i in range(1, 1 << N-1):
    flag = True
    start, sp = [], 0
    link, lp = [], 0
    for j in range(N):
        if i & (1 << j):
            if start:
                for k in start:
                    sp += S[j][k]
            start.append(j)
        else:
            if link:
                for k in link:
                    lp += S[j][k]
            link.append(j)
    ans = min(ans, abs(sp-lp))
print(ans)