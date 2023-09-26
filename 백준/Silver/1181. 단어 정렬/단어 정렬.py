import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    w = input().rstrip()
    if w not in arr:
        arr.append(w)
arr.sort(key=lambda x:(len(x), x))
print(*arr, sep="\n")