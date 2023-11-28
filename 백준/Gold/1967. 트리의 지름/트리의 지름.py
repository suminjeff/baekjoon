import heapq
import sys
input = sys.stdin.readline

from collections import deque

inf = int(1e9)


def find(start):
    visited = [0] * (N+1)
    que = deque()
    que.append([0, start])
    visited[start] = 1
    distance = [-1] * (N+1)
    distance[start] = 0
    while que:
        d, v = que.popleft()

        for nd, nv in graph[v]:
            if not visited[nv]:
                visited[nv] = 1
                cost = d + nd
                distance[nv] = cost
                que.append([cost, nv])
    return max(distance)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, c, w = map(int, input().split())
    graph[p].append([w, c])
    graph[c].append([w, p])


leaf_nodes = []
for v in range(1, N+1):
    leaf = True
    for nd, nv in graph[v]:
        if v < nv:
            leaf = False
            break
    if leaf:
        leaf_nodes.append(v)


ans = 0
for start in leaf_nodes:
    ans = max(ans, find(start))

print(ans)