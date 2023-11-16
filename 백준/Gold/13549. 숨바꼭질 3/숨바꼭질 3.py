import sys
input = sys.stdin.readline

from heapq import heappop, heappush

inf = int(1e9)
MAX = 100000

def dijkstra(start):
    visited = [0] * (MAX+1)
    time = [inf] * (MAX+1)
    visited[start] = 1
    time[start] = 0
    heap = []
    heappush(heap, [time[start], start])

    while heap:
        t, v = heappop(heap)
        if v*2 <= MAX and visited[v*2] == False:
            visited[v*2] = 1
            time[v*2] = min(time[v*2], time[v])
            heappush(heap, [t, v*2])
        if v+1 <= MAX and visited[v+1] == False:
            visited[v+1] = 1
            time[v+1] = min(time[v+1], time[v]+1)
            heappush(heap, [t+1, v+1])
        if v-1 >= 0 and visited[v-1] == False:
            visited[v-1] = 1
            time[v-1] = min(time[v-1], time[v]+1)
            heappush(heap, [t+1, v-1])
    print(time[K])


N, K = map(int, input().split())
dijkstra(N)