import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 1162

N, M, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a-1].append([b-1, t])
    graph[b-1].append([a-1, t])
inf = sys.maxsize
distance = [[inf]*(K+1) for _ in range(N)]
distance[0][0] = 0
heap = [[0, 0, 0]]
while heap:
    t, k, v = heappop(heap)
    if distance[v][k] < t:
        continue
    for nv, nt in graph[v]:
        if distance[nv][k] > t + nt:
            distance[nv][k] = t + nt
            heappush(heap, [t + nt, k, nv])
        if k < K and distance[nv][k+1] > t:
            distance[nv][k+1] = t
            heappush(heap, [t, k+1, nv])
print(min(distance[-1]))