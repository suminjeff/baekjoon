import sys


def solve(n, q, a):
    factorial = [0]*(n+1)
    factorial[0] = 1
    for i in range(1, n+1):
        factorial[i] = factorial[i-1] * i

    visited = [False]*(n+1)

    if q == 1:
        answer = [0]*(n+1)
        k = a[0]
        for i in range(1, n+1):
            cnt = 1
            for j in range(1, n+1):
                if visited[j]:
                    continue
                if k <= cnt * factorial[n-i]:
                    k -= (cnt-1) * factorial[n-i]
                    answer[i] = j
                    visited[j] = True
                    break
                cnt += 1
        print(*answer[1:])

    else:
        k = 1
        for i in range(1, n+1):
            cnt = 0
            for j in range(1, a[i-1]):
                if not visited[j]:
                    cnt += 1
            k += cnt * factorial[n-i]
            visited[a[i-1]] = True
        print(k)


if __name__ == '__main__':
    N = int(input())
    Q, *A = map(int, input().split())
    solve(N, Q, A)
