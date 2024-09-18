import sys


def solve(n, m, edges):
    distance = [[sys.maxsize]*(n+1) for _ in range(n+1)]
    path = [[[i] for i in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        distance[i][i] = 0

    for u, v, c in edges:
        distance[u][v] = min(distance[u][v], c)

    for middle in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                cost = distance[start][middle] + distance[middle][end]
                if cost < distance[start][end]:
                    distance[start][end] = cost
                    path[start][end] = path[start][middle] + path[middle][end]

    for i in range(1, n+1):
        for j in range(1, n+1):
            k = distance[i][j]
            print(k if k != sys.maxsize else 0, end=' ')
        print()

    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] == 0 or distance[i][j] == sys.maxsize:
                print(0)
            else:
                print(len(path[i][j])+1, i, *path[i][j])

    return 0


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    EDGES = [list(map(int, input().split())) for _ in range(M)]
    ANSWER = solve(N, M, EDGES)