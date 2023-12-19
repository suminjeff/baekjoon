import sys
input = sys.stdin.readline


inf = int(1e9)
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
distance = [inf]*(N+1)

def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            curNode, nextNode, cost = edges[j]
            if distance[curNode] != inf and distance[curNode] + cost < distance[nextNode]:
                distance[nextNode] = distance[curNode] + cost
                if i == N-1:
                    return False
    return True


if bellman_ford(1):
    for i in range(2, N+1):
        if distance[i] == inf:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)