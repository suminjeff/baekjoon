import sys
input = sys.stdin.readline

# 17298 오큰수


N = int(input())
A = list(map(int, input().split()))
NGE = [-1]*N
stack = [0]
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)