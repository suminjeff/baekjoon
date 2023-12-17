import sys
input = sys.stdin.readline

from collections import deque


def find(pair):
    r, c = pair
    if (r, c) != parents[r][c]:
        parents[r][c] = find(parents[r][c])
    return parents[r][c]


def union(pair1, pair2):
    parent1, parent2 = find(pair1), find(pair2)
    r1, c1 = parent1
    r2, c2 = parent2
    if r1 < r2:
        parents[r2][c2] = parent1
    elif r1 > r2:
        parents[r1][c1] = parent2
    elif r1 == r2:
        if c1 < c2:
            parents[r2][c2] = parent1
        else:
            parents[r1][c1] = parent2


T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    edges = []
    for r in range(R):
        cost = list(map(int, input().split()))
        for c in range(C-1):
            edges.append([(r, c), (r, c+1), cost[c]])
    for r in range(R-1):
        cost = list(map(int, input().split()))
        for c in range(C):
            edges.append([(r, c), (r+1, c), cost[c]])
    edges.sort(key=lambda x:x[2])
    parents = [[(r, c) for c in range(C)] for r in range(R)]
    ans = 0
    for pair1, pair2, cost in edges:
        parent1, parent2 = find(pair1), find(pair2)
        if parent1 != parent2:
            union(parent1, parent2)
            ans += cost
    print(ans)