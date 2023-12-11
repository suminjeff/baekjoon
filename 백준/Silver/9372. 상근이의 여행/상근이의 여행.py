import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    planes = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for a, b in planes:
        x, y = find(a), find(b)
        if x != y:
            union(x, y)
            ans += 1
    print(ans)