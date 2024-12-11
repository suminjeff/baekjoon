import sys


def solve(n: int, k: int, caffeine: list[int]) -> int:
    inf = sys.maxsize
    caffeine.sort(reverse=True)

    dp = [inf] * (k + 1)
    dp[0] = 0

    for c in caffeine:
        for i in range(k, c-1, -1):
            if i-c >= 0:
                dp[i] = min(dp[i], dp[i-c]+1)
    answer = dp[k]
    return answer if answer != inf else -1


if __name__ == '__main__':
    N, K = map(int, input().split())
    CAFFEINE = list(map(int, input().split()))
    ANSWER = solve(N, K, CAFFEINE)
    print(ANSWER)