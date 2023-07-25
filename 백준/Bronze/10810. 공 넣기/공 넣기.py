N, M = map(int, input().split())

basket = []

for n in range(N):
    basket.append(0)

for m in range(M):
    i, j, k = map(int, input().split())
    for ij in range(i, j+1):
        basket[ij-1] = k

for i in range(N):
    print(basket[i], end=" ")
