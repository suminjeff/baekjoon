import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N = int(input())
parents = [i for i in range(N+1)]
edges = []
for i in range(1, N):
    adj_r = list(map(int, input().split()))
    for j in range(1, N-i+1):
        c = adj_r[j-1]
        edges.append([i, i+j, c])
edges.sort(key=lambda x:x[2])
adj_l = [[] for _ in range(N+1)]
for x, y, c in edges:
    if find(x) != find(y):
        union(x, y)
        adj_l[x].append(y)
        adj_l[y].append(x)

for i in range(1, N+1):
    ans = adj_l[i]
    print(len(ans), *sorted(ans))