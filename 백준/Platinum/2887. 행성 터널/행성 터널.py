import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N = int(input())
planets = [list(map(int, input().split())) for _ in range(N)]
planets_x = []
planets_y = []
planets_z = []
for i in range(N):
    x, y, z = planets[i]
    planets_x.append([x, i])
    planets_y.append([y, i])
    planets_z.append([z, i])

planets_x.sort()
planets_y.sort()
planets_z.sort()

edges = []
for i in range(N-1):
    x1, v1 = planets_x[i]
    x2, v2 = planets_x[i+1]
    edges.append([abs(x1-x2), v1, v2])

    y1, v1 = planets_y[i]
    y2, v2 = planets_y[i+1]
    edges.append([abs(y1-y2), v1, v2])

    z1, v1 = planets_z[i]
    z2, v2 = planets_z[i+1]
    edges.append([abs(z1-z2), v1, v2])
edges.sort()

parents = [i for i in range(N)]

ans = 0
for c, s, e in edges:
    s, e = find(s), find(e)
    if s == e:
        continue
    union(s, e)
    ans += c
print(ans)
