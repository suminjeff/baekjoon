import sys
input = sys.stdin.readline
from collections import deque
# 15591


def bfs(usado, start):
    visited = [0]*(N+1)
    visited[start] = 1
    que = deque([start])
    res = 0
    while que:
        v = que.popleft()
        for nv, nd in graph[v]:
            if visited[nv] == 0:
                visited[nv] = 1
                if nd >= usado:
                    res += 1
                    que.append(nv)
                    visited[nv] = 1
    return res

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])
for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))