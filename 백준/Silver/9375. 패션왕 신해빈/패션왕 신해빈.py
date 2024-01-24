import sys
input = sys.stdin.readline

# 9375

T = int(input())
for tc in range(T):
    N = int(input())
    clothes = {}
    pk = 0
    for _ in range(N):
        product, product_type = input().split()
        if product_type not in clothes:
            clothes.setdefault(product_type, 1)
        else:
            clothes[product_type] += 1
    ans = 1
    for i in clothes:
        ans *= clothes[i]+1
    print(ans-1)
