N = int(input())
arr = [0] + list(map(int, input().split()))

lis = [0]*(N+1)

for i in range(1, N+1):
    lis[i] = 1
    for j in range(i):
        if arr[i] > arr[j]:
            lis[i] = max(lis[i], lis[j]+1)
print(max(lis))