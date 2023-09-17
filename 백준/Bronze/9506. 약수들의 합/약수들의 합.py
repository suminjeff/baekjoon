while True:
    n = int(input())
    if n == -1:
        break
    else:
        res = []
        for i in range(1, n):
            if n % i == 0:
                res.append(i)
        if sum(res) == n:
            print(f"{n} = ", end="")
            print(*res, sep=" + ")
        else:
            print(f"{n} is NOT perfect.")