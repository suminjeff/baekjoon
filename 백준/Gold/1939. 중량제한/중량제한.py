import sys
input = sys.stdin.readline

from heapq import heappop, heappush

inf = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, -c])
    graph[b].append([a, -c])
f1, f2 = map(int, input().split())
weight = [0]*(N+1)
weight[f1] = inf
heap = [[-inf, f1]]
while heap:
    w_lim, v = heappop(heap)
    if v == f2:
        print(-w_lim)
        break
    for nv, w in graph[v]:
        if weight[nv] > w:
            weight[nv] = w
            heappush(heap, [max(w_lim, w), nv])
