import sys


n = int(input())


div, mod = divmod(n, 5)

if div == 0:
    if mod % 2 == 0:
        print(mod // 2)
    else:
        print(-1)
else:
    if mod % 2 == 0:
        print(div + mod // 2)
    else:
        print(div-1 + ((mod+5) // 2))