import sys
from heapq import heappop, heappush


def solve(n, m, a, b, c, edge):
    graph = [[] for _ in range(n+1)]
    for x, y, cost in edge:
        graph[x].append([y, cost])
        graph[y].append([x, cost])

    min_cost = [sys.maxsize] * (n+1)
    # 낸 돈, 현재 위치
    heap = [(0, 0, a)]
    while heap:
        e, cost, v = heappop(heap)
        if min_cost[v] < e:
            continue
        # if v == b: continueS
        for nv, n_cost in graph[v]:
            ne = max(e, n_cost)
            n_cost += cost
            if n_cost <= c and min_cost[nv] > ne:
                min_cost[nv] = ne
                heappush(heap, (ne, n_cost, nv))
    answer = min_cost[b]
    return answer if answer != sys.maxsize else -1


if __name__ == '__main__':
    N, M, A, B, C = map(int, input().split())
    EDGE = [list(map(int, input().split())) for _ in range(M)]
    ANSWER = solve(N, M, A, B, C, EDGE)
    print(ANSWER)