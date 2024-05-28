import sys

# 1956


def floyd_warshall(V, adj):
    dist = [[sys.maxsize]*V for _ in range(V)]

    for u in range(V):
        dist[u][u] = 0

    for u in range(V):
        for v, w in adj[u]:
            dist[u][v] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def find_min_cycle(V, E, edges):
    adj = [[] for _ in range(V)]
    for a, b, c in edges:
        adj[a-1].append((b-1, c))

    dist = floyd_warshall(V, adj)
    min_cycle = sys.maxsize
    for u in range(V):
        for v in range(V):
            if u != v and dist[u][v] < sys.maxsize and dist[v][u] < sys.maxsize:
                min_cycle = min(min_cycle, dist[u][v] + dist[v][u])
    return -1 if min_cycle == sys.maxsize else min_cycle


V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

result = find_min_cycle(V, E, edges)
print(result)