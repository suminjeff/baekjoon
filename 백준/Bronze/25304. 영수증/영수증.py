X = int(input())

N = int(input())

total = 0

for n in range(N):
    a, b = map(int, input().split())
    price = a * b
    total += price

if X == total:
    print("Yes")
else:
    print("No")