def solve(n, grid):
    max_dp = grid[0][:3]
    min_dp = grid[0][:3]

    for r in range(1, n):
        row = grid[r]
        max_dp = [row[0] + max(max_dp[0], max_dp[1]), row[1] + max(max_dp), row[2] + max(max_dp[1], max_dp[2])]
        min_dp = [row[0] + min(min_dp[0], min_dp[1]), row[1] + min(min_dp), row[2] + min(min_dp[1], min_dp[2])]

    return max(max_dp), min(min_dp)


if __name__ == '__main__':
    N = int(input())
    GRID = [list(map(int, input().split())) for _ in range(N)]
    ANSWER = solve(N, GRID)
    print(*ANSWER)