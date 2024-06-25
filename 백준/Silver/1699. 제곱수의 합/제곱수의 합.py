import sys


def solve(n):
    dp = [i for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, i+1):
            k = j*j
            if k > i:
                break
            if dp[i] > dp[i-k]+1:
                dp[i] = dp[i-k]+1
    return dp[-1]


if __name__ == '__main__':
    N = int(input())
    answer = solve(N)
    print(answer)