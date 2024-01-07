import sys
input = sys.stdin.readline

# 4803 트리

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


case = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    parents = [i for i in range(n+1)]
    edges = [list(map(int, input().split())) for _ in range(m)]
    for x, y in edges:
        if find(x) != find(y):
            union(x, y)
        else:
            union(0, min(x, y))
    tree = 0
    for i in range(1, n+1):
        if parents[i] == i:
            tree += 1
    if tree == 0:
        print(f"Case {case}: No trees.")
    elif tree == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {tree} trees.")
    case += 1