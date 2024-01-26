import sys
input = sys.stdin.readline

# 28473

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:(x[2], x[3]))
parents = [i for i in range(N+1)]

ans1, ans2 = "", 0
for x, y, z, w in edges:
    if find(x) != find(y):
        union(x, y)
        ans1 += str(z)
        ans2 += w
if len(ans1) == N-1:
    print(ans1, ans2)
else:
    print(-1)