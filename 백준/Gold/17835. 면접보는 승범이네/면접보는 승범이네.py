import sys
from heapq import heappush, heappop
input = sys.stdin.readline

inf = float('inf')
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[v].append([u, c])
cities = list(map(int, input().split()))
distance = [inf]*(N+1)
heap = []
for city in cities:
    heappush(heap, [0, city])
    distance[city] = 0
while heap:
    d, v = heappop(heap)
    if distance[v] < d:
        continue
    for nv, nd in graph[v]:
        nd += d
        if distance[nv] > nd:
            distance[nv] = nd
            heappush(heap, [nd, nv])
max_d = max(distance[1:])
print(distance.index(max_d))
print(max_d)