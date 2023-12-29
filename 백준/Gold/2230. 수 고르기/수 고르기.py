import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

left = right = 0
res = int(2e9)
while left <= right and right < N:
    if arr[right]-arr[left] < M:
        right += 1
    else:
        res = min(res, arr[right]-arr[left])
        left += 1
print(res)