import sys
input = sys.stdin.readline

# 1541

string = input().split('-')
res = []
for s in string:
    tmp = 0
    if '+' in s:
        s = s.split('+')
        for n in s:
            tmp += int(n)
    else:
        tmp += int(s)
    res.append(tmp)
ans = res[0]
for i in range(1, len(res)):
    ans -= res[i]
print(ans)