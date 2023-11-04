import sys
input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parents[y] = x
        children[x] += children[y]


T = int(input())
for tc in range(1, T+1):
    auto_increment = 0
    F = int(input())
    parents = {}
    children = {}
    for _ in range(F):
        p1, p2 = input().split()
        if p1 not in parents.keys():
            parents[p1], children[p1] = p1, 1
        if p2 not in parents.keys():
            parents[p2], children[p2] = p2, 1
        union(p1, p2)
        print(children[parents[p1]])

