import sys
input = sys.stdin.readline


from heapq import heappop, heappush


# 14284 간선 이어가기 2

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
s, t = map(int, input().split())
inf = int(1e9)
distance = [inf]*(n+1)
distance[s] = 0
heap = [[0, s]]
while heap:
    d, v = heappop(heap)
    for nv, nd in graph[v]:
        nd += d
        if distance[nv] > nd:
            distance[nv] = nd
            heappush(heap, [nd, nv])
print(distance[t])