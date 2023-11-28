import sys
input = sys.stdin.readline
from collections import deque

def find(start):
    que = deque()
    que.append([0, start])
    distance = [-1] * (N+1)
    distance[start] = 0
    while que:
        d, v = que.popleft()

        for nd, nv in graph[v]:
            if distance[nv] == -1:
                cost = d + nd
                distance[nv] = cost
                que.append([cost, nv])
    return distance

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    x, *arr = list(map(int, input().split()))
    for i in range(0, len(arr)-1, 2):
        y, d = arr[i], arr[i+1]
        graph[x].append([d, y])

ans = 0
dist = find(1)
dx = max(dist)
x = dist.index(dx)
ans_dist = find(x)
print(max(ans_dist))