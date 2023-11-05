import sys
input = sys.stdin.readline


def func(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (func(a, b//2, c)**2) % c
    else:
        return (a*func(a, b // 2, c) ** 2) % c


a, b, c = map(int, input().split())
print(func(a, b, c))
