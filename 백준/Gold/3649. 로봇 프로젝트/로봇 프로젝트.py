import sys
input = sys.stdin.readline

# 3649


while True:
    try:
        X = int(input())
        N = int(input())
        L = [int(input()) for _ in range(N)]
        L.sort()
    except:
        break
    NX = X * 10000000
    left, right, flag = 0, N-1, True
    while left < right:
        v = L[left] + L[right]
        if v == NX:
            print("yes", L[left], L[right])
            flag = False
            break
        if v < NX:
            left = left+1
        else:
            right = right-1
    if flag:
        print("danger")