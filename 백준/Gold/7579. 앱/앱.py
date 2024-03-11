import sys

# 7579

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

def solve(N, M, memory, cost):
    K = sum(cost)
    inf = sys.maxsize
    knapsack = [[0]*(K+1) for _ in range(N+1)]
    result = inf
    for i in range(1, N+1):
        m, c = memory[i-1], cost[i-1]
        for j in range(K+1):
            if j < c:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-c]+m)
            if knapsack[i][j] >= M:
                result = min(result, j)
    return result


ans = solve(N, M, memory, cost)
print(ans)
