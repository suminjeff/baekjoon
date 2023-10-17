import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binary_search(s, e):
    global cnt
    if s >= e:
        return

    c = arr[s]+arr[e]
    if c == X:
        cnt += 1
        binary_search(s+1, e-1)
        return

    if c < X:
        binary_search(s+1, e)
    else:
        binary_search(s, e-1)




N = int(input())
arr = sorted(list(map(int, input().split())))
X = int(input())
cnt = 0
binary_search(0, N-1)
print(cnt)