import sys
input = sys.stdin.readline

from heapq import heappush, heappop

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x != 0:
        heappush(heap, [abs(x), -1 if x < 0 else 1])
    else:
        if heap:
            output = heappop(heap)
            if output[1] == -1:
                print(-output[0])
            else:
                print(output[0])
        else:
            print(0)