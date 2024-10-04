def solve(n, schedule):
    dp = [0]*(n+1)
    for day in range(1, n+1):
        t, p = schedule[day-1]
        dp[day] = max(dp[day], dp[day-1])
        end_t = day + t-1
        if end_t <= n:
            dp[end_t] = max(dp[end_t], dp[day-1] + p)
    return dp[n]


if __name__ == '__main__':
    N = int(input())
    SCHEDULE = [list(map(int, input().split())) for _ in range(N)]
    ANSWER = solve(N, SCHEDULE)
    print(ANSWER)