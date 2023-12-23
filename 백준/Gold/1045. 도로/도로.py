import sys
input = sys.stdin.readline

import heapq

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
edges = []
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if arr[i][j] == 'Y':
            cnt += 1
            edges.append([i, j])
if len(edges) < M:
    print(-1)
else:
    edges.sort(key=lambda x:(x[0], x[1]))
    parents = [i for i in range(N)]
    ans = [0]*N
    others = []
    cnt = 0
    for x, y in edges:
        p, q = find(x), find(y)
        if p != q:
            union(p, q)
            ans[x] += 1
            ans[y] += 1
            cnt += 1
        else:
            heapq.heappush(others, [x, y])
    if cnt != N-1:
        print(-1)
    else:
        for _ in range(M-cnt):
            x, y = heapq.heappop(others)
            ans[x] += 1
            ans[y] += 1
        print(*ans)