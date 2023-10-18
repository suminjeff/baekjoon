import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    visited[start] = 1
    que = deque()
    que.append([start, 0])
    while que:
        v, depth = que.popleft()
        if v == T:
            return depth
        for w in family[v]:
            if visited[w] == 0:
                visited[w] = 1
                que.append([w, depth+1])
    return -1


N = int(input())
S, T = map(int, input().split())
M = int(input())
family = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
print(bfs(S))