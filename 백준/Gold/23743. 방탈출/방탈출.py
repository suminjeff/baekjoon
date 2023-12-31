import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
emergency_exits = list(map(int, input().split()))
for i in range(N):
    c = emergency_exits[i]
    edges.append([0, i+1, c])
edges.sort(key=lambda x:x[2])
parents = [i for i in range(N+1)]
ans = 0
for x, y, c in edges:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        ans += c
print(ans)