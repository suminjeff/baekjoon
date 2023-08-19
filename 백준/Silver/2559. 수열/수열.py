N, K = map(int, input().split())
arr = list(map(int, input().split()))

p1 = 0
p2 = K
ans_list = [sum(arr[:K])]

for i in range(N-K):
    ans_list.append(ans_list[-1] - arr[i] + arr[i+K])

ans = max(ans_list)

print(ans)