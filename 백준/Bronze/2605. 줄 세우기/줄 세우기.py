N = int(input())
arr = list(map(int, input().split()))
stack = []

for i in range(N):
    if arr[i] != 0:
        temp = []
        for _ in range(arr[i]):
            temp.append(stack.pop())
        stack.append(i+1)
        for _ in range(arr[i]):
            stack.append(temp.pop())
    else:
        stack.append(i+1)

print(*stack)