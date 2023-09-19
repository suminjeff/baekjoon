N = int(input())

res = []
for num in range(N-1, 0, -1):
    str_n = str(num)
    ns = []
    for i in str_n:
        ns.append(int(i))
    tmp = num + sum(ns)
    if tmp == N:
        res.append(num)
if res:
    print(min(res))
else:
    print(0)