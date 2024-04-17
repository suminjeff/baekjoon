N, M = map(int, input().split())
A = list(map(int, input().split()))
prefix_sum = 0
R = [0]*M

for i in range(N):
    prefix_sum += A[i]
    R[prefix_sum % M] += 1

result = R[0]

for i in range(M):
    result += R[i] * (R[i]-1) // 2

print(result)