import sys
input = sys.stdin.readline

from collections import deque

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
s, e = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(M)]

inf = int(1e9)
parents = [i for i in range(N+1)]
weights = [inf]*(N+1)

bridges.sort(key=lambda x:x[2], reverse=True)

graph = [[] for _ in range(N+1)]
for x, y, w in bridges:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        graph[x].append([y, w])
        graph[y].append([x, w])

visited = [0]*(N+1)
que = deque([[s, inf]])
visited[s] = 1

ans = 0
while que:
    cur_node, cur_weight = que.popleft()
    if cur_node == e:
        ans = cur_weight
        break
    for next_node, next_weight in graph[cur_node]:
        if visited[next_node] == 0:
            visited[next_node] = 1
            new_weight = min(cur_weight, next_weight)
            que.append([next_node, new_weight])
print(ans)