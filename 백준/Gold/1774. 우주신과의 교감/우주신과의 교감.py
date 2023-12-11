import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N, M = map(int, input().split())
gods = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    p, q = find(x), find(y)
    union(p, q)

edges = []
for i in range(N):
    xi, yi = gods[i]
    for j in range(i+1, N):
        xj, yj = gods[j]
        distance = ((xi-xj)**2 + (yi-yj)**2)**(1/2)
        edges.append([i+1, j+1, distance])
edges.sort(key=lambda x:x[2])

ans = 0
for x, y, d in edges:
    p, q = find(x), find(y)
    if p == q:
        continue
    union(p, q)
    ans += d
print(f"{ans:.2f}")

