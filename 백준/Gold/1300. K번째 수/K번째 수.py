import sys


def solve(n, k):
    start, end = 1, k
    answer = -1
    while start <= end:
        mid = (start + end) // 2

        m = 0

        for i in range(1, n+1):
            m += min(mid//i, N)

        if m >= k:
            answer = mid
            end = mid-1
        else:
            start = mid+1

    return answer


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    ANSWER = solve(N, K)
    print(ANSWER)