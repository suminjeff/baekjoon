import sys
input = sys.stdin.readline


N = int(input())
target = N
ans = 0
while True:

    a, b = N//10, N % 10
    c = a + b
    d = c % 10
    N = b*10 + d
    ans += 1
    if N == target:
        print(ans)
        break
