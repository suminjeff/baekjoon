def mean(arr):
    return int(sum(arr)/len(arr))


def median(arr):
    return sorted(arr)[len(arr)//2]


my_arr = []
for n in range(5):
    my_arr.append(int(input()))

print(mean(my_arr))
print(median(my_arr))
