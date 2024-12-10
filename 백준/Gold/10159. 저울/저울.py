import sys


def solve(n: int, m: int, data: list[list[int]]):

    adj_m = [[sys.maxsize if i != j else 1 for j in range(n)] for i in range(n)]

    for a, b in data:
        adj_m[a-1][b-1] = 1


    for middle in range(n):
        for start in range(n):
            for end in range(n):
                adj_m[start][end] = min(adj_m[start][end], adj_m[start][middle] + adj_m[middle][end])


    for i in range(n):
        cnt = 0
        for j in range(n):
            if adj_m[i][j] == sys.maxsize and adj_m[j][i] == sys.maxsize:
                cnt += 1
        print(cnt)


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    DATA = [list(map(int, input().split())) for _ in range(M)]
    solve(N, M, DATA)
