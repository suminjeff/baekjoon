import sys
from heapq import heappop, heappush

inf = sys.maxsize
def dijkstra(start, n, graph):
    distance = [inf]*(n+1)
    distance[start] = 0
    heap = [[0, start]]
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

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for x, y, c in fares:
        graph[x].append([y, c])
        graph[y].append([x, c])
    _s = dijkstra(s, n, graph)
    _a = dijkstra(a, n, graph)
    _b = dijkstra(b, n, graph)
    answer = inf
    for i in range(1, n+1):
        answer = min(answer, _s[i] + _a[i] + _b[i])
    return answer