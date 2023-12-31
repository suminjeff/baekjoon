import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1


def topological_sort():
    que = deque()
    for i in range(1, N+1):
        if degree[i] == 0:
            que.append(i)
    ans = []
    while que:
        v = que.popleft()
        ans.append(v)
        for nv in graph[v]:
            degree[nv] -= 1
            if degree[nv] == 0:
                que.append(nv)
    print(*ans)

topological_sort()
