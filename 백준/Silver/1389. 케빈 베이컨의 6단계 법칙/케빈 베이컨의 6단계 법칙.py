import sys
input = sys.stdin.readline

# 1389

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

inf = sys.maxsize
kevin = []
for i in range(1, N+1):
    visited = [0]*(N+1)
    visited[i] = 1
    que = deque([i])
    while que:
        v = que.popleft()
        for nv in graph[v]:
            if visited[nv] == 0:
                visited[nv] = visited[v] + 1
                que.append(nv)
    kevin.append([i, sum(visited)])
kevin.sort(key=lambda x:(x[1], x[0]))
print(kevin[0][0])