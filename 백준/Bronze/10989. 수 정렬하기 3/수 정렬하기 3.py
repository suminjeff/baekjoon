import sys
st = sys.stdin.readline

N = int(st())
lst = [0] * 10001
for i in range(N):
    lst[int(st())] += 1

for p in range(10001):
    for _ in range(lst[p]):
        print(p)