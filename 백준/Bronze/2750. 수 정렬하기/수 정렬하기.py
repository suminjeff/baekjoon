def my_len(arr):
    length = 0
    for _ in arr:
        length += 1
    return length


def my_max(arr):
    max_v = 0
    for v in arr:
        if max_v < v:
            max_v = v
    return max_v


def my_min(arr):
    min_v = 0
    for v in arr:
        if min_v < v:
            min_v = v
    return min_v


def bubble(arr):
    length = my_len(arr)
    for i in range(length-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def counting(arr):
    max_v = my_max(arr)
    counts = [0 for _ in range(max_v+1)]
    sorted_arr = arr[:]
    for i in range(my_len(arr)):
        counts[arr[i]] += 1
    for i in range(1, my_len(counts)):
        counts[i] += counts[i-1]
    for i in range(my_len(sorted_arr)-1, -1, -1):
        counts[arr[i]] -= 1
        sorted_arr[counts[arr[i]]] = arr[i]
    return sorted_arr


def selection(arr):
    for i in range(my_len(arr)-1):
        minIdx = i
        for j in range(i+1, my_len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr


N = int(input())
num_list = []
for n in range(N):
    num = int(input())
    num_list.append(num)

# bubble(num_list)
# num_list = counting(num_list)
selection(num_list)
print(*num_list, sep="\n")