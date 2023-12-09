import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
rev_arr = list(reversed(arr))

increase = [1]*N
decrease = [1]*N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if rev_arr[i] > rev_arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)
decrease.reverse()

ans = 0
for i in range(N):
    ans = max(ans, increase[i] + decrease[i] - 1)

print(ans)