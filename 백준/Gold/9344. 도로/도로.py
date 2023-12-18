import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


T = int(input())
for tc in range(1, T+1):
    N, M, P, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x:x[2])
    parents = [i for i in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for u, v, w in edges:
        p, q = find(u), find(v)
        if p != q:
            union(p, q)
            graph[u].append(v)
            graph[v].append(u)
    cnt = 0
    for i in range(1, N+1):
        if i == parents[i]:
            cnt += 1
    if cnt == 1 and (Q in graph[P]):
        print("YES")
    else:
        print("NO")