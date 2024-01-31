import sys
input = sys.stdin.readline

# 2458

N, M = map(int, input().split())
inf = sys.maxsize
adj_m = [[inf]*N for _ in range(N)]
parents, children = [0]*(N+1), [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    adj_m[a-1][b-1] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if adj_m[s][e] > adj_m[s][m] + adj_m[m][e]:
                adj_m[s][e] = adj_m[s][m] + adj_m[m][e]

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if adj_m[i][j] != inf or adj_m[j][i] != inf:
            cnt += 1
    if cnt == N-1:
        ans += 1
print(ans)