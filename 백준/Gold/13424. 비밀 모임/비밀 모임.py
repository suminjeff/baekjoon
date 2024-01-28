import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 13424
inf = sys.maxsize
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a-1].append([b-1, c])
        graph[b-1].append([a-1, c])
    K = int(input())
    S = list(map(int, input().split()))
    res = [0]*N
    for s in S:
        distance = [inf]*N
        distance[s-1] = 0
        heap = [[0, s-1]]
        while heap:
            d, v = heappop(heap)
            if distance[v] < d:
                continue
            for nv, nd in graph[v]:
                nd += d
                if distance[nv] > nd:
                    distance[nv] = nd
                    heappush(heap, [nd, nv])
        for i in range(N):
            res[i] += distance[i]
    print(res.index(min(res))+1)