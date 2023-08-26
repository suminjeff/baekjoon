tsn = "369"
N = int(input())
ans = []
for i in range(1, N+1):
    str_i = str(i)
    res = ""
    clap = 0
    for j in str_i:
        if j in tsn:
            clap += 1
    if clap:
        res += "-"*clap
    else:
        res += str_i
    ans.append(res)
print(*ans)