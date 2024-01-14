import sys
input = sys.stdin.readline

# 1107 리모컨


def check_number(number):
    for i in range(len(number)):
        if int(number[i]) in broken:
            return False
    return True


N = int(input())
M = int(input())
broken = list(map(int, input().split()))
min_click = abs(N-100)

for number in range(1000001):
    if check_number(str(number)):
        min_click = min(min_click, abs(number-N)+len(str(number)))
print(min_click)