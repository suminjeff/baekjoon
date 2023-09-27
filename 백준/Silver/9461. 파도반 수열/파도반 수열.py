import sys
input = sys.stdin.readline


MAX = 100
padovan = [0, 1, 1, 1, 2] + [0] * (MAX-4)

for i in range(5, 101):
    padovan[i] = padovan[i-2] + padovan[i-3]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(padovan[N])