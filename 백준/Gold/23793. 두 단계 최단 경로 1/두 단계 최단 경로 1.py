import sys

import heapq


def dijkstra(n: int, graph: list[list[int]], start: int, cross: int = -1) -> list[int]:
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        d, v = heapq.heappop(heap)
        if distance[v] < d:
            continue
        for nv, nd in graph[v]:
            nd += d
            if distance[nv] > nd:
                distance[nv] = nd
                heapq.heappush(heap, [nd, nv])
    return distance


def solve(n: int, m: int, edge: list[list[int]], x: int, y: int, z: int) -> tuple[int, int]:
    graph1 = [[] for _ in range(n+1)]
    graph2 = [[] for _ in range(n+1)]

    for u, v, w in edge:
        graph1[u].append([v, w])
        if u != y and v != y:
            graph2[u].append([v, w])

    _x_y = dijkstra(n, graph1, x)[y]
    _y_z = dijkstra(n, graph1, y)[z]
    _x_z_no_y = dijkstra(n, graph2, x)[z]

    answer1 = _x_y + _y_z
    answer2 = _x_z_no_y

    return answer1 if answer1 < sys.maxsize else -1, answer2 if answer2 < sys.maxsize else -1


if __name__ == '__main__':
    N, M = map(int, input().split())
    EDGE = [list(map(int, input().split())) for _ in range(M)]
    X, Y, Z = map(int, input().split())
    ANSWER = solve(N, M, EDGE, X, Y, Z)
    print(*ANSWER)
