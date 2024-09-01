import sys
from collections import OrderedDict


def solve(k, l, log):
    order = OrderedDict()
    for i in range(l):
        order[log[i]] = i

    sorted_order = sorted(order.items(), key=lambda x:x[1])
    for i in range(k):
        if i < len(sorted_order):
            print(sorted_order[i][0])
        else:
            break

if __name__ == '__main__':
    K, L = map(int, input().split())
    LOG = [input() for _ in range(L)]
    solve(K, L, LOG)
