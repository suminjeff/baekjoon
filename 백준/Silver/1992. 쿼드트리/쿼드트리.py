import sys
input = sys.stdin.readline

# 1992


def divide_conquer(r, c, length):
    global ans
    color = arr[r][c]
    flag = True
    for i in range(r, r+length):
        for j in range(c, c+length):
            if arr[i][j] != color:
                flag = False
                break
        if not flag:
            break

    if flag:
        if color == 1:
            ans += "1"
        else:
            ans += "0"
    else:
        ans += "("
        length //= 2
        divide_conquer(r, c, length)
        divide_conquer(r, c+length, length)
        divide_conquer(r+length, c, length)
        divide_conquer(r+length, c+length, length)
        ans += ")"

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
ans = ""
divide_conquer(0, 0, N)
print(ans)