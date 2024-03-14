import sys

# 9084

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    knapsack = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N+1):
        knapsack[i][0] = 1

    for i in range(1, N+1):
        v = coins[i-1]
        for j in range(M+1):
            knapsack[i][j] = knapsack[i-1][j]
            if j >= v:
                knapsack[i][j] += knapsack[i][j-v]
    print(knapsack[-1][-1])