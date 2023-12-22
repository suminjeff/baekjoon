import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
temp = 0
for n in arr:
    temp += n
    sum_arr.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    ans = sum_arr[j] - sum_arr[i-1]
    print(ans)