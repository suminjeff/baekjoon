import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M = map(int, input().split())
K, *arr = list(map(int, input().split()))
arr.sort()
parents = [i for i in range(N+1)]
for x in arr:
    union(0, x)

party = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    party_n, *party_arr = party[i]
    knows_truth = False
    root = parents[min(party_arr)]
    for x in party_arr:
        p = find(x)
        if p != root:
            union(p, root)

cnt = 0
for i in range(M):
    party_n, *party_arr = party[i]
    flag = True
    for x in party_arr:
        p = find(x)
        if parents[p] == 0:
            flag = False
    if flag:
        cnt += 1
print(cnt)
