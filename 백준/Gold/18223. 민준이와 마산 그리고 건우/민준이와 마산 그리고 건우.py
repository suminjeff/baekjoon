import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(start):
    heap = [[0, start]]
    distance = [inf]*(V+1)
    distance[start] = 0
    while heap:
        d, v = heappop(heap)
        for nv, nd in graph[v]:
            nd += d
            if distance[nv] > nd:
                distance[nv] = nd
                heappush(heap, [nd, nv])
    return distance


inf = sys.maxsize
V, E, P = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
_s, _p = dijkstra(1), dijkstra(P)
minjun_masan, minjun_gunwoo, gunwoo_masan = _s[V], _s[P], _p[V]
if minjun_gunwoo + gunwoo_masan == minjun_masan:
    print("SAVE HIM")
else:
    print("GOOD BYE")