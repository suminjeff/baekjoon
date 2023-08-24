def winner(n):
    if n == 1:
        if A_dict[n] > B_dict[n]:
            return "A"
        elif A_dict[n] < B_dict[n]:
            return "B"
        else:
            return "D"
    else:
        if A_dict[n] > B_dict[n]:
            return "A"
        elif A_dict[n] < B_dict[n]:
            return "B"
        else:
            return winner(n-1)


N = int(input())
for _ in range(N):
    # 별 = 4, 동그라미 = 3, 네모 = 2, 세모 = 1
    A = list(map(int, input().split()))
    a = A.pop(0)
    B = list(map(int, input().split()))
    b = B.pop(0)

    A_dict = {}
    B_dict = {}
    for i in range(1, 5):
        A_dict[i] = A.count(i)
    for j in range(1, 5):
        B_dict[j] = B.count(j)

    print(winner(4))