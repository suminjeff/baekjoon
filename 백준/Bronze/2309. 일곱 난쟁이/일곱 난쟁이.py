N = 9
arr = []

for n in range(N):
    arr.append(int(input()))

subset_list = []
for i in range(1<<N):
    subset = []
    for j in range(N):
        if i & (1<<j):
            subset.append(arr[j])
    subset_list.append(subset)

new_list = []
for i in range(1<<N):
    if len(subset_list[i]) == 7 and sum(subset_list[i]) == 100:
        new_list = sorted(subset_list[i])

for i in new_list:
    print(i)