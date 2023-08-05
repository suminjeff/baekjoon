N = int(input())
arr = list(map(int, input().split()))
M = max(arr)
for i in range(len(arr)):
    arr[i] *= 100/M

print(sum(arr)/N)