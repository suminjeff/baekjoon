import sys
input = sys.stdin.readline

# 2805

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)
while start <= end:
    mid = (start+end)//2

    cut = 0
    for t in tree:
        if t >= mid:
            cut += t-mid

    if cut >= M:
        start = mid+1
    else:
        end = mid-1
print(end)