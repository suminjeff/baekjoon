N, M = map(int, input().split())

basket = []

for n in range(N):
    basket.append(n+1)

for m in range(M):
    i, j = map(int, input().split())
    b1 = basket[i-1]
    b2 = basket[j-1]
    basket[i-1] = b2
    basket[j-1] = b1

for i in range(N):
    print(basket[i], end=" ")
