N = 9
heights = [int(input()) for _ in range(9)]

subsets = []
for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(heights[j])
    subsets.append(subset)

ans = []
for subset in subsets:
    if len(subset) == 7 and sum(subset) == 100:
        ans = sorted(subset)

for i in ans:
    print(i)