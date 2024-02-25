import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 12834

N, V, E = map(int, input().split())
A, B = map(int, input().split())
H = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

inf = sys.maxsize
heap_A = [[0, A]]
distance_A = [inf]*(V+1)
distance_A[A] = 0
while heap_A:
    d, v = heappop(heap_A)
    if distance_A[v] < d:
        continue
    for nv, nd in graph[v]:
        nd += d
        if distance_A[nv] > nd:
            distance_A[nv] = nd
            heappush(heap_A, [nd, nv])

heap_B = [[0, B]]
distance_B = [inf]*(V+1)
distance_B[B] = 0
while heap_B:
    d, v = heappop(heap_B)
    if distance_B[v] < d:
        continue
    for nv, nd in graph[v]:
        nd += d
        if distance_B[nv] > nd:
            distance_B[nv] = nd
            heappush(heap_B, [nd, nv])
ans = 0
for h in H:
    _A = distance_A[h]
    if _A == inf:
        ans += -1
    else:
        ans += _A

    _B = distance_B[h]
    if _B == inf:
        ans += -1
    else:
        ans += _B
print(ans)
