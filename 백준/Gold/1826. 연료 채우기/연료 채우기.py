import sys
from heapq import heappush, heappop

if __name__ == '__main__':
    N = int(input())
    gas_station = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0], -x[1]))

    L, P = map(int, input().split())
    gas_station.append([L, 0])

    heap = []
    cnt = 0

    for a, b in gas_station:
        if P >= L:
            break
        while P < a and heap:
            P += -heappop(heap)
            cnt += 1
        if P < a:
            break
        heappush(heap, -b)

    print(cnt if P >= L else -1)