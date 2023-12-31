import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def topological_sort():
    heap = []
    for i in range(1, N+1):
        if degree[i] == 0:
            heappush(heap, i)
    ans = []
    while heap:
        v = heappop(heap)
        ans.append(v)
        for nv in graph[v]:
            degree[nv] -= 1
            if degree[nv] == 0:
                heappush(heap, nv)
    print(*ans)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

topological_sort()
