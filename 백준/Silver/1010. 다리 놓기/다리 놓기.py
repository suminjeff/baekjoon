import sys
input = sys.stdin.readline


def factorial(n, depth, target):
    if depth == target:
        return n
    return n * factorial(n-1, depth+1, target)


def nCr(n, r):
    return factorial(n, 1, r)//factorial(r, 1, r)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = max(N, M)
    r = min(N, M)
    ans = nCr(n, r)
    print(ans)