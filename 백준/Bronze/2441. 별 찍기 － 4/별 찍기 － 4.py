N = int(input())

for n in range(N, 0, -1):
    space = " "
    star = n * "*"
    print(space * (N - n) + star)