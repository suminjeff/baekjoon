

def solve(n, m, a):
    answer = 0

    start, end = 0, 1
    _sum = 0

    while end <= n:
        tmp = sum(a[start:end])
        if tmp <= m:
            if tmp == m:
                answer += 1
            end += 1
        else:
            start += 1

    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ANSWER = solve(N, M, A)
    print(ANSWER)