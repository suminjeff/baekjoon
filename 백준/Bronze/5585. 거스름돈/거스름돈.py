n = int(input())

coin = [500, 100, 50, 10, 5, 1]
cnt = 0

money = 1000 - n

for i in coin:
    cnt += money // i
    money %= i

print(cnt)