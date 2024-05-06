import sys
from heapq import heappop, heappush

# 5944


def dijkstra(node):
    distance = [INF]*(P+1)
    distance[node] = 0
    heap = [[0, node]]

    while heap:
        d, v = heappop(heap)

        if distance[v] < d:
            continue

        for nv, nd in graph[v]:
            nd += d
            if distance[nv] > nd:
                distance[nv] = nd
                heappush(heap, [nd, nv])
    return distance


INF = sys.maxsize
C, P, PB, PA1, PA2 = map(int, input().split())
graph = [[] for _ in range(P+1)]
for _ in range(C):
    P1_i, P2_i, D_i = map(int, input().split())
    graph[P1_i].append([P2_i, D_i])
    graph[P2_i].append([P1_i, D_i])

_PB = dijkstra(PB)
_PA1 = dijkstra(PA1)
_PA2 = dijkstra(PA2)

# PB -> PA1 -> PA2
route1 = _PB[PA1] + _PA1[PA2]

# PB -> PA2 -> PA1
route2 = _PB[PA2] + _PA2[PA1]

ans = min(route1, route2)

print(ans)