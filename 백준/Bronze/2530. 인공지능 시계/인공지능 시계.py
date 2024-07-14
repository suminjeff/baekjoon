# 2530
A, B, C = map(int, input().split())
T = A*60*60 + B*60 + C
M = 24*60*60
D = int(input())

E = T + D

hour = (E // (60*60)) % 24

E %= 60*60

minute = E // 60

E %= 60

second = E

print(hour, minute, second)