import math

M = int(input())
color = list(map(int, input().split()))
K = int(input())
N = sum(color)
total = math.comb(N, K)
same_color = 0
for s in color:
    same_color += math.comb(s, K)

print(same_color/total)