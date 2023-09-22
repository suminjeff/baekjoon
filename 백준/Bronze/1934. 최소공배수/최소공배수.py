import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    if A % B == 0 or B % A == 0:
        print(max(A, B))
    else:
        pA, pB = A, B
        while A != B:
            if A < B:
                A += pA
            elif B < A:
                B += pB
        print(A)