import sys

from heapq import heappop, heappush

def solve(n, d, edges):
    graph = [[] for _ in range(d+1)]

    for i in range(1, d+1):
        graph[i-1].append([i, 1])

    for a, b, c in edges:
        if b <= d:
            graph[a].append([b, c])

    heap = []
    heappush(heap, [0, 0])  # 현재까지의 거리, 현재 위치

    distance = [sys.maxsize] * (d+1)
    distance[0] = 0

    while heap:
        dist, node = heappop(heap)
        if distance[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            next_dist += dist

            if distance[next_node] > next_dist:
                distance[next_node] = next_dist
                heappush(heap, [next_dist, next_node])
    return distance[d]


if __name__ == "__main__":
    N, D = map(int, input().split())
    EDGES = [list(map(int, input().split())) for _ in range(N)]
    ANSWER = solve(N, D, EDGES)
    print(ANSWER)