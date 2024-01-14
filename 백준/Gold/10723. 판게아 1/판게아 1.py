import sys
input = sys.stdin.readline

# 10723 판게아 1


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    edges = []
    for i in range(1, N):
        u, c = map(int, input().split())
        edges.append([i, u, c])
    res = []
    for i in range(M):
        parents = [i for i in range(N)]
        u, v, c = map(int, input().split())
        edges.append([u, v, c])
        edges.sort(key=lambda x:x[2])
        mst = 0
        for x, y, c in edges:
            if find(x) != find(y):
                union(x, y)
                mst += c
        res.append(mst)
    ans = res[0]
    for i in range(1, M):
        ans = ans ^ res[i]
    print(ans)