import sys
input = sys.stdin.readline

from heapq import heappop, heappush

inf = int(1e9)

def dijkstra(start):
    distance = [inf] * (N+1)
    distance[start] = 0
    heap = []
    heappush(heap, [distance[start], start])
    while heap:
        d, v = heappop(heap)

        if distance[v] < d:
            continue

        for nd, w in adj_l[v]:
            dist = d + nd
            if distance[w] > dist:
                distance[w] = dist
                heappush(heap, (dist, w))
    return distance


N, E = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj_l[a].append((c, b))
    adj_l[b].append([c, a])
v1, v2 = map(int, input().split())

distance = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)

v1_first = distance[v1] + distance_v1[v2] + distance_v2[N]
v2_first = distance[v2] + distance_v2[v1] + distance_v1[N]

ans = min(v1_first, v2_first)
print(ans if ans < inf else -1)