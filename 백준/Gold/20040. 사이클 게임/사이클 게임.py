import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return "CYCLE"
    parent[max(x, y)] = min(x, y)
    return "CONTINUE"


N, M = map(int, input().split())
parent = [p for p in range(N)]
cycle = False
for i in range(1, M+1):
    x, y = map(int, input().split())
    if union(x, y) == "CYCLE":
        cycle = True
        print(i)
        break
if not cycle:
    print(0)