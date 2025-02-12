n = int(input())
answer = 0
honey = list(map(int, input().split()))
prefix_sum = [0]*n
prefix_sum[0] = honey[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + honey[i]

for i in range(1, n-1):
    answer = max(answer, prefix_sum[n-2] + prefix_sum[i-1] - honey[i])

for i in range(1, n-1):
    answer = max(answer, prefix_sum[n-1] - honey[0] + prefix_sum[n-1] - prefix_sum[i] - honey[i])

for i in range(1, n-1):
    answer = max(answer, prefix_sum[n-2] - honey[0] + honey[i])
print(answer)
