import sys
input = sys.stdin.readline


def dfs(string, depth, v, c):
    if depth == L:
        if v >= 1 and c >= 2:
            ans.append(string)
        return
    for i in range(C):
        if ord(string[-1]) < ord(arr[i]) and not used[i]:
            if arr[i] in "aeiou":
                used[i] = 1
                dfs(string+arr[i], depth+1, v+1, c)
                used[i] = 0
            else:
                used[i] = 1
                dfs(string+arr[i], depth+1, v, c+1)
                used[i] = 0

ans = []
L, C = map(int, input().split())
arr = sorted(list(input().split()))
used = [0]*C
for i in range(1, 1 << C):
    subset = []
    for j in range(C):
        if i & (1 << j):
            subset.append(arr[j])
    if len(subset) == L:
        v = c = 0
        for k in range(L):
            if subset[k] in "aeiou":
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            ans.append("".join(subset))
ans.sort()
#
# for i in range(L):
#     used[i] = 1
#     if arr[i] in "aeiou":
#         dfs(arr[i], 1, 1, 0)
#     else:
#         dfs(arr[i], 1, 0, 1)
#     used[i] = 0
# ans.sort()
print(*ans, sep="\n")