N = int(input())

for n in range(1, N + 1):
    space = " "
    star = n * "*"
    print(space * (N - n) + star)