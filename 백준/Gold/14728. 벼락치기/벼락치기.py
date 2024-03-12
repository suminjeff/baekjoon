import sys

# 14728

N, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

knapsack = [[0]*(T+1) for _ in range(N+1)]
for i in range(1, N+1):
    k, s = data[i-1]
    for j in range(T+1):
        if j < k:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-k]+s)
print(knapsack[-1][-1])