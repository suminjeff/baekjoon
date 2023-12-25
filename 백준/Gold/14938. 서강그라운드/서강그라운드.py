import sys
input = sys.stdin.readline

from heapq import heappop, heappush

inf = int(1e9)
N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

ans = 0
for start in range(1, N+1):
    distance = [inf]*(N+1)
    distance[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        d, v = heappop(heap)
        for nv, l in graph[v]:
            nd = d + l
            if nd <= M and nd < distance[nv]:
                distance[nv] = nd
                heappush(heap, [nd, nv])
    d = 0
    for node in range(1, N+1):
        if distance[node] != inf:
            d += items[node]
    ans = max(ans, d)
print(ans)