import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for i in range(1, N+1):
    num = str(i)
    cnt += num.count("3")
    cnt += num.count("6")
    cnt += num.count("9")
print(cnt)