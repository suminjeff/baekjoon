import sys
input = sys.stdin.readline


def f(n):
    zero, one = [1, 0, 1], [0, 1, 1]
    if n > 2:
        for i in range(2, n):
            zero.append(zero[i-1] + zero[i])
            one.append(one[i-1] + one[i])
    print(f"{zero[n]} {one[n]}")

T = int(input())
for tc in range(T):
    N = int(input())
    f(N)

