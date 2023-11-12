import sys
input = sys.stdin.readline
import heapq

INF = 10e9

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distances[start] = 0

    while heap:
        distance, now = heapq.heappop(heap)

        if distances[now] < distance:
            continue

        for new_distance, new_node in adj_l[now]:
            cum_distance = distance + new_distance
            if cum_distance < distances[new_node]:
                distances[new_node] = cum_distance
                heapq.heappush(heap, (cum_distance, new_node))


N = int(input())
M = int(input())
adj_l = [[] for _ in range(N+1)]
distances = [INF] * (N+1)
for _ in range(M):
    s, e, w = map(int, input().split())
    adj_l[s].append([w, e])
S, E = map(int, input().split())
dijkstra(S)
print(distances[E])
