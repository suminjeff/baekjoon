import sys
input = sys.stdin.readline


T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    arr = [[0]*n for _ in range(k+1)]
    arr[0] = [i+1 for i in range(n)]
    for i in range(1, k+1):
        for j in range(n):
            arr[i][j] = sum(arr[i-1][:j+1])
    print(arr[k][n-1])
