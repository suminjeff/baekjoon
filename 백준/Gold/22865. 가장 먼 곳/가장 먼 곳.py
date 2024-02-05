import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 22865


N = int(input())
friends = list(map(int, input().split()))
A, B, C = friends
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    u, v, c = map(int, input().split())
    graph[u].append([v, c])
    graph[v].append([u, c])

inf = sys.maxsize
result = [inf]*N
ans = inf
for x in [A, B, C]:
    distance = [inf]*(N+1)
    distance[x] = 0
    heap = [[0, x]]
    while heap:
        d, v = heappop(heap)
        if distance[v] < d:
            continue
        for nv, nd in graph[v]:
            nd += d
            if distance[nv] > nd:
                distance[nv] = nd
                heappush(heap, [nd, nv])
    for i in range(N):
        result[i] = min(result[i], distance[i+1])
print(result.index(max(result))+1)
