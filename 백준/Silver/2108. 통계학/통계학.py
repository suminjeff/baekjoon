import sys
input = sys.stdin.readline


def avg(arr):
    global N
    return round(sum(arr) / N)


def median(arr):
    global N
    arr.sort()
    return arr[N//2]


def mode(arr):
    idx = {}
    for n in arr:
        n = 4000+n
        if n in idx.keys():
            idx[n] += 1
        else:
            idx.setdefault(n, 1)
    max_cnt = max(idx.values())
    res = []
    for k, v in idx.items():
        if v == max_cnt:
            res.append(k - 4000)
    if len(res) > 1:
        return res[1]
    else:
        return res[0]


def print_range(arr):
    arr.sort()
    return arr[-1] - arr[0]


N = int(input())
n_list = [int(input()) for _ in range(N)]
print(avg(n_list))
print(median(n_list))
print(mode(n_list))
print(print_range(n_list))

