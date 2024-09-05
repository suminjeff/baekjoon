import sys
from collections import deque


def solve(n, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = [_ for _ in range(n+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        p, q = find(x), find(y)
        if p != q:
            parent[max(p, q)] = parent[min(p, q)]
            return {'msg': 'success'}
        else:
            parent[x] = parent[y] = 0
            return {'msg': 'cycle', 'start': min(x, y), 'end': max(x, y)}

    is_cycle = [False]*(n+1)
    cycle_start, cycle_end = int(), int()
    for u, v in edges:
        result = union(u, v)
        if result.get('msg') == 'cycle':
            cycle_start = result.get('start')
            cycle_end = result.get('end')
            is_cycle[cycle_start] = True
            is_cycle[cycle_end] = True

    visited = [0]*(n+1)
    visited[cycle_start] = visited[cycle_end] = 1
    que = deque([[cycle_start, str(cycle_start)]])

    while que:
        v, path = que.popleft()

        for nv in graph[v]:
            if visited[nv] == 0:
                visited[nv] = 1
                que.append([nv, path+' '+str(nv)])
            else:
                if nv == cycle_end:
                    cycle_list = list(map(lambda x:int(x), path.split()[1:]))
                    if not cycle_list:
                        continue
                    for cv in cycle_list:
                        is_cycle[cv] = True
                    break
    distance = [-1]*(n+1)
    cycle_que = deque()
    for v in range(1, n+1):
        if is_cycle[v]:
            cycle_que.append(v)
            distance[v] = 0

    while cycle_que:
        v = cycle_que.pop()
        for nv in graph[v]:
            if distance[nv] == -1:
                distance[nv] = distance[v] + 1
                cycle_que.append(nv)
    return distance[1:]


if __name__ == '__main__':
    N = int(input())
    EDGES = [list(map(int, input().split())) for _ in range(N)]
    ANSWER = solve(N, EDGES)
    print(*ANSWER)