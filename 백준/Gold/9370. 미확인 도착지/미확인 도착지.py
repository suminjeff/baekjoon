import sys
input = sys.stdin.readline

from heapq import heappop, heappush


def dijkstra(s):
    distance = [inf] * (n + 1)
    distance[s] = 0
    heap = []
    heappush(heap, [0, s])
    while heap:
        k, v = heappop(heap)
        for nv, d in graph[v]:
            nd = k + d
            if distance[nv] > nd:
                distance[nv] = nd
                heappush(heap, [nd, nv])
    return distance


inf = int(1e9)
T = int(input())
for tc in range(1, T + 1):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    _s = dijkstra(s)
    _g = dijkstra(g)
    _h = dijkstra(h)
    ans = []
    for _ in range(t):
        x = int(input())
        if (_s[g] + _g[h] + _h[x] == _s[x]) or (_s[h] + _h[g] + _g[x] == _s[x]):
            ans.append(x)
    print(*sorted(ans))
