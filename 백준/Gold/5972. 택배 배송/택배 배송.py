import sys
input = sys.stdin.readline

from heapq import heappop, heappush


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

inf = int(1e9)
food = [inf]*(N+1)
heap = [[0, 1]]
while heap:
    f, v = heappop(heap)
    if food[v] < f:
        continue
    for nv, nf in graph[v]:
        nf += f
        if food[nv] > nf:
            food[nv] = nf
            heappush(heap, [nf, nv])
print(food[N])
