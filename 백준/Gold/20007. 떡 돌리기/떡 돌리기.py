import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 20007

N, M, X, Y = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
inf = sys.maxsize
distance = [inf]*N
distance[Y] = 0
heap = [[0, Y]]
while heap:
    d, v = heappop(heap)
    if distance[v] < d:
        continue
    for nv, nd in graph[v]:
        nd += d
        if distance[nv] > nd:
            distance[nv] = nd
            heappush(heap, [nd, nv])
order = []
for i, v in enumerate(distance):
    if i == Y:
        continue
    heappush(order, [v, i])
current_distance = 0
day = 1
flag = True
while order:
    dist, house = heappop(order)
    round_trip = dist*2
    if X - (current_distance + round_trip) >= 0:
        current_distance += round_trip
    else:
        if round_trip > X:
            flag = False
            break
        current_distance = round_trip
        day += 1
if flag:
    print(day)
else:
    print(-1)