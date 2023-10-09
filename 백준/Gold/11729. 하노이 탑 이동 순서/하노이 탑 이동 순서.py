import sys
input = sys.stdin.readline

def hanoi(n, start, end, other):
    global cnt
    if n == 1:
        cnt += 1
        res.append([start, end])
    else:
        hanoi(n-1, start, other, end)
        cnt += 1
        res.append([start, end])
        hanoi(n-1, other, end, start)


N = int(input())
cnt = 0
res = []
hanoi(N, 1, 3, 2)
print(cnt)
for s, e in res:
    print(s, e)