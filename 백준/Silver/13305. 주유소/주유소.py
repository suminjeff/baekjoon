# 13305
N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
ans = 0

# 내가 쓸 리터당 가격
p = price[0]
for i in range(N-1):
    # 만약 현재 위치에서의 리터당 가격이 이전 위치의 리터당 가격보다 싸다면
    if p > price[i]:
        # 내가 쓸 리터당 가격을 바꿔주기
        p = price[i]
    # 총 비용에 내가 쓸 리터당 가격 * 거리를 더해줌
    ans += p * road[i]
print(ans)