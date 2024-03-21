import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 1240

def dijkstra(n, adj_l, start):
    inf = sys.maxsize
    distance = [inf]*(n+1)
    distance[start] = 0
    heap = [[0, start]]
    while heap:
        d, v = heappop(heap)
        if distance[v] < d:
            continue
        for nv, nd in adj_l[v]:
            nd += d
            if distance[nv] > nd:
                distance[nv] = nd
                heappush(heap, [nd, nv])
    return distance


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y, c = map(int, input().split())
    graph[x].append([y, c])
    graph[y].append([x, c])



for _ in range(M):
    a, b = map(int, input().split())
    dist = dijkstra(N, graph, a)
    print(dist[b])