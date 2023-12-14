import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p, q = find(x), find(y)
    parents[max(p, q)] = min(p, q)


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
parents = [i for i in range(N)]
edges = []
total = 0
for i in range(N):
    for j in range(N):
        v = arr[i][j]
        if v.isalpha():
            if v.isupper():
                arr[i][j] = ord(v)-38
                if i != j:
                    edges.append([i, j, arr[i][j]])
            elif v.islower():
                arr[i][j] = ord(v)-96
                if i != j:
                    edges.append([i, j, arr[i][j]])
            total += arr[i][j]
edges.sort(key=lambda x:x[2])
mst = 0
for x, y, c in edges:
    p, q = find(x), find(y)
    if p != q:
        union(p, q)
        mst += c

cnt = 0
for i in range(N):
    if i == parents[i]:
        cnt += 1


if cnt == 1:
    ans = total - mst
else:
    ans = -1
print(ans)
