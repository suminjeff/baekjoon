import sys
input = sys.stdin.readline

from itertools import combinations

N, K = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(N)]
used = [0]*N

ans = int(1e9)
for subset in combinations(range(N), K):
    res = 0
    for n in range(N):
        if n in subset:
            continue
        min_distance = int(1e9)
        x1, y1 = houses[n]
        for k in subset:
            x2, y2 = houses[k]
            distance = abs(x1-x2) + abs(y1-y2)
            min_distance = min(min_distance, distance)
        res = max(res, min_distance)
    ans = min(ans, res)
print(ans)