import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])
inf = sys.maxsize
distance = [0]+[inf]*(N-1)
heap = [[0, 0]]
while heap:
    d, v = heappop(heap)
    if distance[v] < d:
        continue
    for nv, nd in graph[v]:
        nd += d
        if distance[nv] > nd and arr[nv] == 0:
            distance[nv] = nd
            heappush(heap, [nd, nv])
ans = distance[N-1]
print(ans if ans != inf else -1)