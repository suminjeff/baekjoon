import heapq
import sys

N = int(input())
classes = []
for _ in range(N):
    S, T = map(int, input().split())
    classes.append((S, T))

classes.sort()

min_heap = []
heapq.heappush(min_heap, classes[0][1])

for i in range(1, N):
    earliest_end = min_heap[0]

    if classes[i][0] >= earliest_end:
        heapq.heappop(min_heap)

    heapq.heappush(min_heap, classes[i][1])

print(len(min_heap))