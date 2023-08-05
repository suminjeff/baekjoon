N, M = map(int, input().split())
arr = [n for n in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = reversed(arr[i-1:j])
print(*arr)
