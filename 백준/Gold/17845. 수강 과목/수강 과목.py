import sys


def solve(n: int, k: int, data: list[list[int]]) -> int:
    knapsack = [[0]*(n+1) for _ in range(k+1)]
    for x in range(1, k+1):
        i, t = data[x-1]
        for y in range(n+1):
            knapsack[x][y] = knapsack[x-1][y]

            if y >= t:
                knapsack[x][y] = max(knapsack[x][y], knapsack[x-1][y-t]+i)
    answer = knapsack[-1][-1]
    return answer


if __name__ == '__main__':
    N, K = map(int, input().split())
    DATA = [list(map(int, input().split())) for _ in range(K)]
    ANSWER = solve(N, K, DATA)
    print(ANSWER)