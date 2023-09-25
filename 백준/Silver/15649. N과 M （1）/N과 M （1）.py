import sys
input = sys.stdin.readline


def perm(arr, n):
    global N
    if len(arr) == n:
        print(*arr)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            arr.append(input_arr[i])
            perm(arr, n)
            arr.pop()
            visited[i] = 0



N, M = map(int, input().split())
input_arr = [n for n in range(1, N+1)]

visited = [0]*N

perm([], M)