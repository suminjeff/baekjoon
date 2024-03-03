import sys
input = sys.stdin.readline

# 2473

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_value = sys.maxsize
ans = []
for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        value = arr[i] + arr[left] + arr[right]
        if min_value > abs(value):
            min_value = abs(value)
            ans = [arr[i], arr[left], arr[right]]
        if value < 0:
            left += 1
        elif value > 0:
            right -= 1
        else:
            break
print(*ans)
