import sys
sys.setrecursionlimit(10**5)


def solve(n, q, edge):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        parent[max(x, y)] = min(x, y)

    parent = [_ for _ in range(n+1)]
    edge.sort(key=lambda x: (x[2], x[3]))

    mst = 0
    cnt = 0
    last_time = 0
    for x, y, c, t in edge:
        p, q = find(x), find(y)
        if p != q:
            union(p, q)
            mst += c
            cnt += 1
            last_time = max(last_time, t)

    if cnt != n-1:
        return [-1]

    return [last_time, mst]



if __name__ == '__main__':
    N, Q = map(int, input().split())
    EDGE = [list(map(int, input().split())) for _ in range(Q)]
    ANSWER = solve(N, Q, EDGE)
    print(*ANSWER)