import sys

from collections import deque


def bfs(flow: list[list[int]], capacity: list[list[int]], source: int, sink: int) -> list:
    que = deque([source])
    parent = [-1]*SIZE
    parent[source] = source
    while que:
        v = que.popleft()
        for nv in range(SIZE):
            if parent[nv] == -1 and capacity[v][nv] - flow[v][nv] > 0:
                que.append(nv)
                parent[nv] = v
    return parent


def max_flow(capacity: list[list[int]], source: int, sink: int) -> int:
    flow = [[0]*SIZE for _ in range(SIZE)]
    result = 0

    while True:
        parent = bfs(flow, capacity, source, sink)
        if parent[sink] == -1:
            return result
        p = sink
        amount = sys.maxsize
        while p != source:
            amount = min(amount, capacity[parent[p]][p] - flow[parent[p]][p])
            p = parent[p]
        result += amount

        p = sink
        while p != source:
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]


def solve(n: int, pipe: list[list]) -> int:

    capacity = [[0]*SIZE for _ in range(SIZE)]  # r에서 c까지의 용량
    for i in range(n):
        p, q, c = pipe[i]
        p, q = ord(p), ord(q)
        capacity[p][q] += c
        capacity[q][p] += c

    answer = max_flow(capacity, ord("A"), ord("Z"))

    return answer

if __name__ == '__main__':
    SIZE = 128
    N = int(input())
    PIPE = [list(map(lambda x: int(x) if x.isnumeric() else x, input().split())) for _ in range(N)]
    ANSWER = solve(N, PIPE)
    print(ANSWER)