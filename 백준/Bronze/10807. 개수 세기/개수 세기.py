N = int(input())
N_list = list(map(int, input().split()))
v = int(input())
count = 0

for n in N_list:
    if v == n:
        count += 1

print(count)