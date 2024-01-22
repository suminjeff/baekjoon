import sys
input = sys.stdin.readline

# 27498

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
parents = [i for i in range(N+1)]
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:(-x[3], -x[2]))
total, love = 0, 0
for x, y, c, d in edges:
    total += c
    if find(x) != find(y):
        union(x, y)
        love += c
print(total-love)