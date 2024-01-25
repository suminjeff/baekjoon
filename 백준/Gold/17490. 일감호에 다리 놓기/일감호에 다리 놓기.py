import sys
input = sys.stdin.readline

# 17490

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N, M, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
block = {}
for i in range(M):
    a, b = map(int, input().split())
    t = (min(a, b), max(a, b))
    if t not in block:
        block.setdefault(t, 1)
if M <= 1:
    print("YES")
else:
    parents = [i for i in range(N+1)]
    edges = []
    for i in range(N):
        a, b = 1 + i, 1 + (i+1) % N
        edges.append([0, a, S[a]])
        if (min(a, b), max(a, b)) in block:
            continue
        union(a, b)
    edges.sort(key=lambda x:x[2])
    cnt = 0
    for x, y, c in edges:
        if find(x) != find(y):
            union(x, y)
            cnt += c
    if cnt <= K:
        print("YES")
    else:
        print("NO")