import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    P = input().rstrip()
    N = int(input().rstrip())
    arr = input().rstrip().strip("[]").split(sep=",")
    idx = 0
    ans = ''
    for p in P:
        if p == "R":
            idx = N-1 - idx
        else:
            if idx >= N or idx < 0:
                ans = 'error'
                break
            else:
                if arr[idx] == "":
                    ans = 'error'
                    break
                if idx == 0:
                    arr.pop(0)
                    N -= 1
                elif idx == N-1:
                    arr.pop()
                    N -= 1
                    idx = N-1
    if ans:
        print(ans)
    else:
        if idx == 0:
            print("["+",".join(arr)+"]")
        else:
            print("["+",".join(reversed(arr))+"]")

