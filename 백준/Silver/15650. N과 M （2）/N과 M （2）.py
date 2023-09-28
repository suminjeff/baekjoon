import sys
input = sys.stdin.readline


def combination(start, k, end):
    if start == end:
        print(*c)
        return
    for i in range(k, N):
        c[start] = arr[i]
        combination(start+1, i+1, end)


N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
c = [0] * M
combination(0, 0, M)