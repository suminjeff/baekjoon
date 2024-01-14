import sys
input = sys.stdin.readline

# 4792 레드 블루 스패닝 트리

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break
    edges = {'B': [], 'R': []}
    for _ in range(m):
        c, f, t = input().split()
        edges[c].append([int(f), int(t)])

    # 파랑을 최대로 하는 트리 = 빨강이 최소가 되는 트리
    parents = [i for i in range(n+1)]
    max_b = 0
    for x, y in edges['B']:
        if find(x) != find(y):
            union(x, y)
            max_b += 1
    for x, y in edges['R']:
        if find(x) != find(y):
            union(x, y)
    root = 0
    for v in range(1, n+1):
        if parents[v] == v:
            root += 1

    # 빨강을 최대로 하는 트리 = 파랑이 최소가 되는 트리
    parents = [i for i in range(n+1)]
    min_b = 0
    for x, y in edges['R']:
        if find(x) != find(y):
            union(x, y)
    for x, y in edges['B']:
        if find(x) != find(y):
            union(x, y)
            min_b += 1
    root = 0
    for v in range(1, n+1):
        if parents[v] == v:
            root += 1
    print(1 if min_b <= k <= max_b else 0)