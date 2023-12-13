import sys
input = sys.stdin.readline

from collections import deque


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N, M = map(int, input().split())
roads = []
total = 0
for _ in range(M):
    s, e, c = list(map(int, input().split()))
    total += c
    roads.append([s, e, c])
roads.sort(key=lambda x:x[2])
parents = [i for i in range(N+1)]

mst = 0
for x, y, cost in roads:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        mst += cost
ans = total - mst


cnt = 0
for i in range(1, N):
    if parents[i] == i:
        cnt += 1
if cnt == 1:
    print(ans)
else:
    print(-1)